import random

from pico2d import *



class Boss:
    PIXEL_PER_METER = (10.0 / 0.2)
    RUN_SPEED_KMPH = 10
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image=None
    def __init__(self):
        self.x,self.y=1000,5500
        self.dir=1
        if Boss.image == None:
            self.image = load_image('./Resource/character/Boss3.png')

                # dragon_death.wav
    def update(self,frame_time):
        distance = Boss.RUN_SPEED_PPS * frame_time
        self.y -= (self.dir * distance)

        if self.y <=500:
            self.y=500
        if  self.y<=1000:
            self.x-=(self.dir*distance)
            self.x=400


    def draw(self):
        self.image.clip_draw(0, 0, 500, 400, self.x, self.y)

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




