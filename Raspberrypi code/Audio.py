import pygame # use pygame instead
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init() # initializes pygame
import time
import datetime

class Audio(pygame.mixer.Sound):
    def __init__(self, path):
        super().__init__(path)
        self.length = datetime.timedelta(seconds=self.get_length())
        self.last_start = datetime.datetime(1, 1, 1)
        self.not_stopped = False
        
    def playSound(self):
        try:
            self.not_stopped = True
            self.last_start = datetime.datetime.now()
            self.play()
        except:
            print("Unable to play audio")
        
        
    def stopSound(self):
        try:
            self.stop()
            self.not_stopped = False
        except:
            print("Couldn't stop sound")
        
    def playWaitUntilDone(self):
        self.playSound()
        time.sleep(self.length)
        
    def isPlaying(self):
        if self.not_stopped or (datetime.datetime.now() > (self.last_start+self.length)):
            return False # is not currently playing audio
        else:
            return True
        
# Audio("harp.wav").play()
# print("hi")
# p = Audio("piano.wav")
# p.play()
# time.sleep(1)
# print(p.isPlaying())
# p.stopSound()
# print(p.isPlaying())