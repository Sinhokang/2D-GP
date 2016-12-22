import random

from pico2d import *


class Attack:

    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 10
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image=None
    def __init__(self,x,y):
        self.x, self.y = x, y +1000
        self.dir = -1
        if Attack.image == None:
            self.image = load_image('./Resource/object/weapon/lightning.png')

    def update(self, frame_time):
        distance = Attack.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)


    def draw(self):
            self.image.clip_draw(0,0,64,100,self.x, self.y)


    def get_bb(self):
        return self.x - 20, self.y-100, self.x + 20, self.y

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
