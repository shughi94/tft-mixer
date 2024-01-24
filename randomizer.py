import random
import os


class Randomizer:
    FILE_PATH = "tracks"
    INSTRUMENTS = ["drums", "main"]
    KEEP_TOGETHER_TRACK_CHANCE = 91 # when choosing 2 tracks, this is the % chance of keeping together drums + main of same genre

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
    ENHANCES_WEIGHT = [25, 3, 3, 2, 1]

    ######## MIXES ########
    TRACK_COUNT = [2, 3, 4, 5]
    TRACK_COUNT_WEIGHT_EARLY = [
        8,
        8,
        1,
        0,
    ]
    TRACK_COUNT_WEIGHT_LATE = [
        8,
        8,
        5,
        2,
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

    def _appendTrack(self, genre, when, instrument):
        file = ""
        # fucking hyperpop do not have drums early
        if genre == "hyperpop" and when == "early" and instrument == "drums":
            file = self.FILE_PATH + os.sep + "hyperpop_early_main.ogg"
        else:
            file = self.FILE_PATH + os.sep + genre + "_" + when + "_" + instrument + ".ogg"
        if file not in self.mix:
            self.mix.append(file)

    def _getRandomDrums(self, when):
        genre = self._getRandomGenre()
        self._appendTrack(genre, when, "drums")

    def _getRandomMain(self, when):
        genre = self._getRandomGenre()
        self._appendTrack(genre, when, "main")

    def _appendBothInstruments(self, genre, when):
        # append both main and drums
        for instrument in self.INSTRUMENTS:
            self._appendTrack(genre, when, instrument)
        # maybe add secondary
        if genre in self.SECONDARY:
            # print("found secondary: " + genre)
            if random.random() < self.SECONDARY_CHANCE / 100:
                self._appendTrack(genre, when, "secondary")

    def _appendTwoTracks(self, when):
        if random.random() < self.KEEP_TOGETHER_TRACK_CHANCE / 100:
            genre = self._getRandomGenre()
            self._appendBothInstruments(genre, when)
        else:
            genre = self._getRandomGenre()
            self._appendTrack(genre, when, "drums")
            genre = self._getRandomGenre()
            self._appendTrack(genre, when, "main")

    def _appendSingleTrack(self, when):
        genre = self._getRandomGenre()
        instrument_list = self.INSTRUMENTS
        instrument = "main"
        if genre in self.SECONDARY:  # REMOVE?
            instrument_list = ["main", "drums", "secondary"]
            instrument = random.choices(instrument_list, [1, 1, 1])[0]
        else:
            instrument = random.choices(self.INSTRUMENTS)[0]
        self._appendTrack(genre, when, instrument)

    def _getMix(self, count, when):
        match count:
            case 2:
                self._appendTwoTracks(when)
            case 3:
                self._appendTwoTracks(when)
                self._getRandomMain(when)
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
        all_mains = [track for track in self.mix if "main" in track]
        if len(all_mains) == 1 and any("hyperpop" in track for track in all_mains):
            self._getRandomMain(self.when)

        # maestro and jazz together do not go well
        if any("jazz" in track for track in self.mix) and any(
            "maestro" in track for track in self.mix
        ):  # remove jazz fuck that
            self.mix = list(filter(lambda track: "jazz" not in track, self.mix))
        # small chance of no drums if hyperpop is selected
        if not any("drums" in track for track in self.mix):
            self._getRandomDrums(self.when)
        # 3 drums too much?
        # early with 4/5 too much?
        return True

    def getRandomMix(self):
        #### WHEN ####
        when_choice = random.choices(self.WHEN, self.WHEN_WEIGHT)[0]
        self.when = when_choice

        #### MIX ####
        self.mix = []

        # early tracks do not mesh well with lots of stuff -> different weights
        if when_choice == "late":
            count_choice = random.choices(
                self.TRACK_COUNT, self.TRACK_COUNT_WEIGHT_LATE
            )[0]
        else:
            count_choice = random.choices(
                self.TRACK_COUNT, self.TRACK_COUNT_WEIGHT_EARLY
            )[0]
        self._getMix(count_choice, when_choice)

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
