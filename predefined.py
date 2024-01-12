import random


class EnhancesEarly:
    maestro = "./tracks/maestro_early.ogg"
    illbeats = "./tracks/illbeats_early.ogg"
    mixmaster = "./tracks/mixmaster_early.ogg"
    jazz = "./tracks/jazz_early.ogg"


class EnhancesLate:
    maestro = "./tracks/maestro_late.ogg"
    illbeats = "./tracks/illbeats_late.ogg"
    mixmaster = "./tracks/mixmaster_late.ogg"
    jazz = "./tracks/jazz_late.ogg"


class GenresEarly:
    country = [
        "./tracks/country_early_drums.ogg",
        "./tracks/country_early_main.ogg",
    ]
    pentakill = [
        "./tracks/pentakill_early_drums.ogg",
        "./tracks/pentakill_early_main.ogg",
        "./tracks/pentakill_early_secondary.ogg",
    ]
    heartsteel = [
        "./tracks/heartsteel_early_drums.ogg",
        "./tracks/heartsteel_early_main.ogg",
        "./tracks/heartsteel_early_secondary.ogg",
    ]
    bit = [
        "./tracks/8bit_early_drums.ogg",
        "./tracks/8bit_early_main.ogg",
    ]
    disco = [
        "./tracks/disco_early_drums.ogg",
        "./tracks/disco_early_main.ogg",
    ]
    kda = [
        "./tracks/kda_early_drums.ogg",
        "./tracks/kda_early_main.ogg",
        "./tracks/kda_early_secondary.ogg",
    ]
    emo = [
        "./tracks/emo_early_drums.ogg",
        "./tracks/emo_early_main.ogg",
    ]
    edm = [
        "./tracks/edm_early_drums.ogg",
        "./tracks/edm_early_main.ogg",
    ]
    punk = [
        "./tracks/punk_early_drums.ogg",
        "./tracks/punk_early_main.ogg",
    ]
    truedamage = [
        "./tracks/truedamage_early_drums.ogg",
        "./tracks/truedamage_early_main.ogg",
        "./tracks/truedamage_early_secondary.ogg",
    ]
    hyperpop = ["./tracks/hyperpop_early_main.ogg"]


class GenresLate:
    country = [
        "./tracks/country_late_drums.ogg",
        "./tracks/country_late_main.ogg",
    ]
    disco = [
        "./tracks/disco_late_drums.ogg",
        "./tracks/disco_late_main.ogg",
    ]
    bit = [
        "./tracks/8bit_late_drums.ogg",
        "./tracks/8bit_late_main.ogg",
    ]
    heartsteel = [
        "./tracks/heartsteel_late_drums.ogg",
        "./tracks/heartsteel_late_main.ogg",
        "./tracks/heartsteel_late_secondary.ogg",
    ]
    pentakill = [
        "./tracks/pentakill_late_drums.ogg",
        "./tracks/pentakill_late_main.ogg",
        "./tracks/pentakill_late_secondary.ogg",
    ]
    kda = [
        "./tracks/kda_late_drums.ogg",
        "./tracks/kda_late_main.ogg",
        "./tracks/kda_late_secondary.ogg",
    ]
    emo = [
        "./tracks/emo_late_drums.ogg",
        "./tracks/emo_late_main.ogg",
    ]
    edm = [
        "./tracks/edm_late_drums.ogg",
        "./tracks/edm_late_main.ogg",
    ]
    punk = [
        "./tracks/punk_late_drums.ogg",
        "./tracks/punk_late_main.ogg",
    ]
    truedamage = [
        "./tracks/truedamage_late_drums.ogg",
        "./tracks/truedamage_late_main.ogg",
        "./tracks/truedamage_late_secondary.ogg",
    ]
    hyperpop = ["./tracks/hyperpop_late_drums.ogg", "./tracks/hyperpop_late_main.ogg"]


class Pogs:
    combos = [
        [
            "./tracks/hyperpop_late_drums.ogg",
            "./tracks/hyperpop_late_main.ogg",
            "./tracks/emo_late_drums.ogg",
            "./tracks/pentakill_late_secondary.ogg",
            "./tracks/mixmaster_late.ogg",
            "./tracks/illbeats_late.ogg",
        ],
        [
            "./tracks/disco_late_drums.ogg",
            "./tracks/disco_late_main.ogg",
            "./tracks/hyperpop_late_main.ogg",
            "./tracks/illbeats_late.ogg",
        ],
    ]

    def getRandomPog(self):
        return random.choice(self.combos)

    def getThePog(self):
        return [
            "./tracks/country_early_drums.ogg",
            "./tracks/country_early_main.ogg",
        ]
