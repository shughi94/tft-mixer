import sys
from predefined import Pogs, GenresEarly, GenresLate, EnhancesEarly, EnhancesLate
from player import Player
from randomizer import Randomizer

from pprint import pprint


def args2tracks(args):
    tracks = []

    predefined = GenresEarly
    predefined_enhance = EnhancesEarly
    if "--late" in args:
        predefined = GenresLate
        predefined_enhance = EnhancesLate

    # main genre
    for arg in args:
        match arg:
            case "--random":
                tracks = Randomizer().getRandomMix()
                continue
            case "--pogs":
                tracks = Pogs().getRandomPog()
                continue
            case "--country":
                tracks += predefined.country
            case "--pentakill":
                tracks += predefined.pentakill
            case "--heartsteel":
                tracks += predefined.heartsteel
            case "--truedamage":
                tracks += predefined.truedamage
            case "--kda":
                tracks += predefined.kda
            case "--disco":
                tracks += predefined.disco
            case "--8bit":
                tracks += predefined.bit
            case "--emo":
                tracks += predefined.emo
            case "--punk":
                tracks += predefined.punk
            case "--edm":
                tracks += predefined.edm
            case "--hyperpop":
                tracks += predefined.hyperpop
            case _:
                pass
    # add enhances
    for arg in args:
        match arg:
            case "--jazz":
                tracks.append(predefined_enhance.jazz)
            case "--illbeats":
                tracks.append(predefined_enhance.illbeats)
            case "--mixmaster":
                tracks.append(predefined_enhance.mixmaster)
            case "--maestro":
                tracks.append(predefined_enhance.maestro)
            case _:
                pass

    pprint(tracks)
    return tracks

tracks = args2tracks(sys.argv)

player = Player(volume=0.5, frequency=44100, buffer=4096)
player.overlay_multiple_ogg(tracks)
player.play_track()
