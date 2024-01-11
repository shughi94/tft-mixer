import os 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame, time

from pydub import AudioSegment

from randomizer import Mixer
from pogs import Pogs 
from pprint import pprint

COMPLETE_FILE = "tracks" + os.sep + "final.ogg"

def play_track(file):
    pygame.mixer.init(48000, -16, 1, 2048)
    channel = pygame.mixer.Channel(0)
    channel.set_volume(0.5)
    sound = pygame.mixer.Sound(file)
    channel.play(sound)

    # wait until it finishes
    while channel.get_busy():
        time.sleep(1)

    pygame.mixer.quit()

    return True


def overlay_multiple_ogg(files):
    # clear existing final ogg
    if os.path.exists(COMPLETE_FILE):
        os.remove(COMPLETE_FILE)

    # combine ogg by overlay
    first = True
    combined = None
    for file in files:
        sound = AudioSegment.from_ogg(file)
        if "maestro" in file:
            sound = sound - 3.5  # decrese decibel, -10 too max
        old_combined = combined
        if first:
            combined = sound
            first = False
        else:
            combined = old_combined.overlay(sound)

    # export combined file
    combined.export(COMPLETE_FILE, format="ogg")
    return COMPLETE_FILE


if __name__ == "__main__":
    # get random mix
    #files = Mixer().getRandomMix()
    files = Pogs().getThePog()
    print("\n")
    pprint(files)

    # create final track
    final = overlay_multiple_ogg(files)

    # Play the final track
    play_track(final)
