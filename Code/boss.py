import random

from pico2d import *



class Boss:
    image=None
    def __init__(self):
        self.x,self.y=400,300
        self.bossUP=True
        self.life=15
        if Boss.image == None:
            self.image = load_image('./Resource/character/Boss.png')

    def draw(self):
        self.image.draw(self.x,self.y)


    def get_bb(self):
        return self.bx - 100, self.by - 100, self.bx + 100, self.by + 200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
