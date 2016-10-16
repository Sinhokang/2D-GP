import random

from pico2d import *





class Background:
    def __init__(self):
        self.image = load_image('C:/DragonFlight/Resource/background/01.png')
        self.image2=load_image('C:/DragonFlight/Resource/background/01.png')
        self.frame=0

    def update(self):
        self.frame -= 3.0
        if self.frame <= -600:
            self.frame = 0

    def draw(self):
        #self.image.clip_draw(0, 0, 800, 600, 400, 600 + self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 100+self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 700+self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 1300 + self.frame)


