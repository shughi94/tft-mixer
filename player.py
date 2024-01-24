import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame, time

from pydub import AudioSegment


class Player:
    COMPLETE_FILE = "tracks" + os.sep + "final.ogg"

    def __init__(self, volume=0.5, frequency=44100, buffer=512) -> None:
        self.buffer = buffer
        self.frequency = frequency
        self.volume = volume

    def play_track(self):
        pygame.mixer.init(self.frequency, -16, 2, self.buffer)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.load(self.COMPLETE_FILE)
        pygame.mixer.music.play()

        # wait until it finishes
        while pygame.mixer.music.get_busy():
            time.sleep(1)

        pygame.mixer.quit()

        return True

    def overlay_multiple_ogg(self, files):
        # clear existing final ogg
        if os.path.exists(self.COMPLETE_FILE):
            os.remove(self.COMPLETE_FILE)

        # combine ogg by overlay
        first = True
        combined = None
        for file in files:
            sound = AudioSegment.from_ogg(file)
            # if "maestro" in file:
            #     sound = sound - 3.5  # decrese decibel, -10 max
            if "jazz" in file:
                sound = sound - 2.5  # decrese decibel, -10 max
            old_combined = combined
            if first:
                combined = sound
                first = False
            else:
                combined = old_combined.overlay(sound) 

        # export combined file
        combined.export(self.COMPLETE_FILE, format="ogg") ## TODO ADD BITRATE?
        return self.COMPLETE_FILE
