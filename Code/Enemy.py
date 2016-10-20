import random

from pico2d import *





class Monster:
    def __init__(self):
        self.x, self.y = 400, 550
        self.frame = 0
        self.state=0
        self.image = load_image('../Resource/character/Enemy2.png')


    def update(self):
        self.frame -= 20.0
        if self.frame <= -600:
            self.frame = 0
        #self.state=(self.state+1)%4
        #elay(0.01)

    def draw(self):
        self.image.clip_draw(0,0, 500,70, self.x, self.y+self.frame)