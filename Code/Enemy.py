import random

from pico2d import *





class Monster:


    PIXEL_PER_METER = (1000.0/ 0.3)
    RUN_SPEED_KMPH = 0.5
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.x, self.y = 400, 550
        self.frame = 0
        self.state=0
        self.image = load_image('../Resource/character/Enemy2.png')
        self.dir =1

    def update(self,frame_time):
        distance =Monster.RUN_SPEED_PPS*frame_time
        self.y-=(self.dir*distance)
        if self.y <= -550:
            self.y = 550

    def draw(self):
        self.image.clip_draw(0,0, 500,70, self.x, self.y)
    def get_bb(self):
        return self.x-22,self.y-25,self.x+22,self.y+25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())