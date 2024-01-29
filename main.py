import sys
from predefined import Pogs, GenresEarly, GenresLate, EnhancesEarly, EnhancesLate
from player import Player
from randomizer import Randomizer

from pprint import pprint


def _get_predefined_genre(arg, predefined):
    tracks = []

    match arg:
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

    return tracks


def args_to_tracks(args):
    tracks = []

    if len(args) == 1:
        args.append("--random")

    predefined = GenresEarly
    predefined_enhance = EnhancesEarly
    if "--late" in args:
        predefined = GenresLate
        predefined_enhance = EnhancesLate

    for arg in args:
        tmp_tracks = []

        arg_array = arg.split("_")
        genre = arg_array[0]

        if arg == "--random":
            tracks = Randomizer().getRandomMix()
            continue
        elif arg == "--pogs":
            tracks = Pogs().getRandomPog()
            continue
        else:
            tmp_tracks = _get_predefined_genre(genre, predefined)

        # if arg has prefix of _m, _d, _s -> filter by main, drum or secondary
        if len(arg_array) > 1:
            match arg_array[1]:
                case "m":
                    # use _main only out of tmp_tracks
                    tmp_tracks = [s for s in tmp_tracks if "_main" in s]
                case "d":
                    # use _drums only out of tmp_tracks
                    tmp_tracks = [s for s in tmp_tracks if "_drums" in s]
                case "s":
                    # use _secondary only out of tmp_tracks
                    tmp_tracks = [s for s in tmp_tracks if "_secondary" in s]
                case "_":
                    pass
        tracks += tmp_tracks

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


loop = False
if "--loop" in sys.argv:
    loop = True

first_time = True
while first_time or loop:
    first_time = False
    tracks = args_to_tracks(sys.argv)
    player = Player(volume=0.5, frequency=44100, buffer=4096)
    player.overlay_multiple_ogg(tracks)
    player.play_track()
    print("\n")
