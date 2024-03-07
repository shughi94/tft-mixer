import random

TRACK_FOLDER = "new_tracks"

class EnhancesEarly:
    maestro = "./"+TRACK_FOLDER+"/maestro_early.ogg"
    illbeats = "./"+TRACK_FOLDER+"/illbeats_early.ogg"
    mixmaster = "./"+TRACK_FOLDER+"/mixmaster_early.ogg"
    jazz = "./"+TRACK_FOLDER+"/jazz_early.ogg"
    piano = "./"+TRACK_FOLDER+"/piano_early.ogg"


class EnhancesLate:
    maestro = "./"+TRACK_FOLDER+"/maestro_late.ogg"
    illbeats = "./"+TRACK_FOLDER+"/illbeats_late.ogg"
    mixmaster = "./"+TRACK_FOLDER+"/mixmaster_late.ogg"
    jazz = "./"+TRACK_FOLDER+"/jazz_late.ogg"
    piano = "./"+TRACK_FOLDER+"/piano_late.ogg"


class GenresEarly:
    country = [
        "./"+TRACK_FOLDER+"/country_early_drums.ogg",
        "./"+TRACK_FOLDER+"/country_early_main.ogg",
    ]
    pentakill = [
        "./"+TRACK_FOLDER+"/pentakill_early_drums.ogg",
        "./"+TRACK_FOLDER+"/pentakill_early_main.ogg",
        "./"+TRACK_FOLDER+"/pentakill_early_secondary.ogg",
    ]
    heartsteel = [
        "./"+TRACK_FOLDER+"/heartsteel_early_drums.ogg",
        "./"+TRACK_FOLDER+"/heartsteel_early_main.ogg",
        "./"+TRACK_FOLDER+"/heartsteel_early_secondary.ogg",
    ]
    bit = [
        "./"+TRACK_FOLDER+"/8bit_early_drums.ogg",
        "./"+TRACK_FOLDER+"/8bit_early_main.ogg",
    ]
    disco = [
        "./"+TRACK_FOLDER+"/disco_early_drums.ogg",
        "./"+TRACK_FOLDER+"/disco_early_main.ogg",
    ]
    kda = [
        "./"+TRACK_FOLDER+"/kda_early_drums.ogg",
        "./"+TRACK_FOLDER+"/kda_early_main.ogg",
        "./"+TRACK_FOLDER+"/kda_early_secondary.ogg",
    ]
    emo = [
        "./"+TRACK_FOLDER+"/emo_early_drums.ogg",
        "./"+TRACK_FOLDER+"/emo_early_main.ogg",
    ]
    edm = [
        "./"+TRACK_FOLDER+"/edm_early_drums.ogg",
        "./"+TRACK_FOLDER+"/edm_early_main.ogg",
    ]
    punk = [
        "./"+TRACK_FOLDER+"/punk_early_drums.ogg",
        "./"+TRACK_FOLDER+"/punk_early_main.ogg",
    ]
    truedamage = [
        "./"+TRACK_FOLDER+"/truedamage_early_drums.ogg",
        "./"+TRACK_FOLDER+"/truedamage_early_main.ogg",
        "./"+TRACK_FOLDER+"/truedamage_early_secondary.ogg",
    ]
    hyperpop = ["./"+TRACK_FOLDER+"/hyperpop_early_main.ogg"]


class GenresLate:
    country = [
        "./"+TRACK_FOLDER+"/country_late_drums.ogg",
        "./"+TRACK_FOLDER+"/country_late_main.ogg",
    ]
    disco = [
        "./"+TRACK_FOLDER+"/disco_late_drums.ogg",
        "./"+TRACK_FOLDER+"/disco_late_main.ogg",
    ]
    bit = [
        "./"+TRACK_FOLDER+"/8bit_late_drums.ogg",
        "./"+TRACK_FOLDER+"/8bit_late_main.ogg",
    ]
    heartsteel = [
        "./"+TRACK_FOLDER+"/heartsteel_late_drums.ogg",
        "./"+TRACK_FOLDER+"/heartsteel_late_main.ogg",
        "./"+TRACK_FOLDER+"/heartsteel_late_secondary.ogg",
    ]
    pentakill = [
        "./"+TRACK_FOLDER+"/pentakill_late_drums.ogg",
        "./"+TRACK_FOLDER+"/pentakill_late_main.ogg",
        "./"+TRACK_FOLDER+"/pentakill_late_secondary.ogg",
    ]
    kda = [
        "./"+TRACK_FOLDER+"/kda_late_drums.ogg",
        "./"+TRACK_FOLDER+"/kda_late_main.ogg",
        "./"+TRACK_FOLDER+"/kda_late_secondary.ogg",
    ]
    emo = [
        "./"+TRACK_FOLDER+"/emo_late_drums.ogg",
        "./"+TRACK_FOLDER+"/emo_late_main.ogg",
    ]
    edm = [
        "./"+TRACK_FOLDER+"/edm_late_drums.ogg",
        "./"+TRACK_FOLDER+"/edm_late_main.ogg",
    ]
    punk = [
        "./"+TRACK_FOLDER+"/punk_late_drums.ogg",
        "./"+TRACK_FOLDER+"/punk_late_main.ogg",
    ]
    truedamage = [
        "./"+TRACK_FOLDER+"/truedamage_late_drums.ogg",
        "./"+TRACK_FOLDER+"/truedamage_late_main.ogg",
        "./"+TRACK_FOLDER+"/truedamage_late_secondary.ogg",
    ]
    hyperpop = ["./"+TRACK_FOLDER+"/hyperpop_late_drums.ogg", "./"+TRACK_FOLDER+"/hyperpop_late_main.ogg"]


class Pogs:
    combos = [
        [
            "./"+TRACK_FOLDER+"/hyperpop_late_drums.ogg",
            "./"+TRACK_FOLDER+"/hyperpop_late_main.ogg",
            "./"+TRACK_FOLDER+"/emo_late_drums.ogg",
            "./"+TRACK_FOLDER+"/pentakill_late_secondary.ogg",
            "./"+TRACK_FOLDER+"/mixmaster_late.ogg",
            "./"+TRACK_FOLDER+"/illbeats_late.ogg",
        ],
        [
            "./"+TRACK_FOLDER+"/disco_late_drums.ogg",
            "./"+TRACK_FOLDER+"/disco_late_main.ogg",
            "./"+TRACK_FOLDER+"/hyperpop_late_main.ogg",
            "./"+TRACK_FOLDER+"/jazz_late.ogg",
        ],
        [
            "./"+TRACK_FOLDER+"/punk_late_drums.ogg",
            "./"+TRACK_FOLDER+"/punk_late_main.ogg",
            "./"+TRACK_FOLDER+"/illbeats_late.ogg",
        ],
    ]

    def getRandomPog(self):
        return random.choice(self.combos)

    def getThePog(self):
        return [
            "./"+TRACK_FOLDER+"/country_early_drums.ogg",
            "./"+TRACK_FOLDER+"/country_early_main.ogg",
        ]
