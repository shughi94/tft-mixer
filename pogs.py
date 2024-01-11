import random


class Pogs:
    ultra_pog = [
        "./tracks/country_early_drums.ogg",
        "./tracks/country_early_main.ogg",
    ]

    tracks = [
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
        [
            "./tracks/country_early_drums.ogg",
            "./tracks/country_early_main.ogg",
        ],
    ]

    def getRandomPog(self):
        return random.choice(self.tracks)

    def getThePog(self):
        return self.ultra_pog
