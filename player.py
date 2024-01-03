import pygame, time, os

from pydub import AudioSegment

from randomizer import Mixer
from pprint import pprint

COMPLETE_FILE = "tracks"+os.sep+"final.ogg"


def play_track(file):
    pygame.mixer.init()
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

    # combine ogg
    first = True
    combined = None
    for file in files:
        sound = AudioSegment.from_ogg(file)
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
    files = Mixer().getRandomMix()
    print("\n")
    pprint(files)

    # create final track
    final = overlay_multiple_ogg(files)

    # Play the final track
    play_track(final)
