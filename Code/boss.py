import random

from pico2d import *



class Boss:
    image=None
    def __init__(self):
        self.x,self.y=400,300
        self.bossUP=True
        self.life=15
        self.rate=1
        if Boss.image == None:
            self.image = load_image('./Resource/character/Boss.png')


    def update(self,frame_time):
        self.rate+=1
        print(self.rate)
        if(self.rate>100):
            self.bossUP=False

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        if (self.bossUP == False):
            self.image.clip_draw(0, 0, 300, 400, self.x, self.y)


    def get_bb(self):
        return self.bx - 100, self.by - 100, self.bx + 100, self.by + 200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


