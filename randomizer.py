import random
import os


class Randomizer:
    FILE_PATH = "tracks"
    INSTRUMENTS = ["drums", "main"]
    KEEP_TOGETHER_TRACK_CHANCE = 85  # when choosing 2 tracks, this is the % chance of keeping together drums + main of same genre

    ######## GENRES ########
    GENRES = [
        "heartsteel",
        "truedamage",
        "kda",
        "edm",
        "8bit",
        "disco",
        "hyperpop",
        "punk",
        "country",
        "pentakill",
        "emo",
    ]
    GENRES_WEIGHT = [5, 5, 7, 1, 5, 6, 6, 6, 8, 6, 5]

    ######## ENHANCES ########
    ENHANCES = ["nope", "mixmaster", "illbeats", "maestro", "jazz"]
    ENHANCES_WEIGHT = [16, 2, 2, 1, 1]

    ######## MIXES ########
    TRACK_COUNT = [2, 3, 4, 5]
    TRACK_COUNT_WEIGHT = [
        10,
        8,
        2,
        1,
    ]
    ######## WHEN ########
    WHEN = ["early", "late"]
    WHEN_WEIGHT = [1, 1]

    ######## SECONDARY #######
    SECONDARY = ["kda", "heartsteel", "pentakill"]
    SECONDARY_WEIGHT = [3, 2, 3]
    SECONDARY_CHANCE = (
        90  # % chance of adding a secondary when 2 of same genre are selected
    )

    def __init__(self):
        self.mix = []
        self.selected_genres = []
        self.selected_files = []

    def _getRandomGenre(self):
        count = 0
        # CHECK HOW TO DO IT BETTER?
        genre = random.choices(self.GENRES, self.GENRES_WEIGHT)[0]
        while genre in self.selected_genres or count < 8:
            genre = random.choices(self.GENRES, self.GENRES_WEIGHT)[0]
            count = count + 1

        self.selected_genres.append(genre)

        return genre

    def _getRandomDrums(self, when):
        genre = self._getRandomGenre()
        file = self.FILE_PATH + os.sep + genre + "_" + when + "_drums.ogg"
        self.mix.append(file)

    def _getRandomMain(self, when):
        genre = self._getRandomGenre()
        file = self.FILE_PATH + os.sep + genre + "_" + when + "_main.ogg"
        self.mix.append(file)

    def _appendBothInstruments(self, genre, when):
        # fucking hyperpop do not have drums early
        if genre == "hyperpop" and when == "early":
            file = self.FILE_PATH + os.sep + genre + "_" + when + "_main.ogg"
            self.mix.append(file)
            # I guess append a fucking random drums part
            self._getRandomDrums(when)
        else:
            # append both main and drums
            for instrument in self.INSTRUMENTS:
                file = (
                    self.FILE_PATH
                    + os.sep
                    + genre
                    + "_"
                    + when
                    + "_"
                    + instrument
                    + ".ogg"
                )
                self.mix.append(file)
        # maybe add secondary
        if genre in self.SECONDARY:
            # print("found secondary: " + genre)
            if random.random() < self.SECONDARY_CHANCE / 100:
                self._appendSecondaryTrack(genre, when)

    def _appendTwoTracks(self, when):
        if random.random() < self.KEEP_TOGETHER_TRACK_CHANCE / 100:
            genre = self._getRandomGenre()
            self._appendBothInstruments(genre, when)
        else:
            genre = self._getRandomGenre()
            file = self.FILE_PATH + os.sep + genre + "_" + when + "_" + "drums.ogg"
            self.mix.append(file)
            genre = self._getRandomGenre()
            file = self.FILE_PATH + os.sep + genre + "_" + when + "_" + "main.ogg"
            self.mix.append(file)

    def _appendSingleTrack(self, when):
        genre = self._getRandomGenre()
        instrument_list = self.INSTRUMENTS
        instrument = "main"
        if genre in self.SECONDARY:  # REMOVE?
            instrument_list = ["main", "drums", "secondary"]
            instrument = random.choices(instrument_list, [3, 3, 2])[0]
        else:
            instrument = random.choices(self.INSTRUMENTS)[0]
        file = self.FILE_PATH + os.sep + genre + "_" + when + "_" + instrument + ".ogg"
        if file not in self.mix:
            self.mix.append(file)

    def _appendSecondaryTrack(self, genre, when):
        file = self.FILE_PATH + os.sep + genre + "_" + when + "_secondary.ogg"
        if file not in self.mix:
            self.mix.append(file)

    def _appendTracks(self, count, when):
        match count:
            case 2:
                self._appendTwoTracks(when)
            case 3:
                self._appendTwoTracks(when)
                self._appendSingleTrack(when)
            case 4:
                self._appendTwoTracks(when)
                self._appendTwoTracks(when)
            case 5:
                self._appendTwoTracks(when)
                self._appendTwoTracks(when)
                self._appendSingleTrack(when)
            case _:
                print("COUNT=NaN WTF")

        return self.mix

    def _lastTouch(self):
        # hyperpop main alone bad
        all_mains = [string for string in self.mix if "main" in string]

        if len(all_mains) == 1 and any("hyperpop" in string for string in all_mains):
            self._getRandomMain(self.when)
        # 3 drums too much?
        return True

    def getRandomMix(self):
        #### WHEN ####
        when_choice = random.choices(self.WHEN, self.WHEN_WEIGHT)[0]
        self.when = when_choice

        #### MIX ####
        self.mix = []
        count_choice = random.choices(self.TRACK_COUNT, self.TRACK_COUNT_WEIGHT)[0]
        self._appendTracks(count_choice, when_choice)

        # #### SECONDARY ####
        # if random.random() < self.SECONDARY_CHANCE / 100:
        #     secondary_choice = random.choices(self.SECONDARY, self.SECONDARY_WEIGHT)[0]
        #     self._appendSecondaryTrack(secondary_choice, when_choice)

        #### ENHANCES ####
        enhances_final = []
        for i in range(0, 3):
            enhances_choice = random.choices(self.ENHANCES, self.ENHANCES_WEIGHT)[0]
            if enhances_choice not in enhances_final:
                enhances_final.append(enhances_choice)
                if enhances_choice != "nope":
                    self.mix.append(
                        self.FILE_PATH
                        + os.sep
                        + enhances_choice
                        + "_"
                        + when_choice
                        + ".ogg"
                    )
        self._lastTouch()

        return self.mix
