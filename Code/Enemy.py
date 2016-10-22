import random

from pico2d import *





class Monster:

    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH =20.0
    RUN_SPEED_MPM=(RUN_SPEED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPM/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS*PIXEL_PER_METER)

    def __init__(self):
        self.x, self.y = 400, 550
        self.frame = 0
        self.state=0
        self.image = load_image('../Resource/character/Enemy2.png')


    def update(self,frame_time):
        #distance =Monster.RUN_SPEED_PPS*frame_time
        #self.total_frame+=1.0
        self.frame -= 10.0
        if self.frame <= -600:
            self.frame = 0
        #self.state=(self.state+1)%4
        #elay(0.01)

    def draw(self):
        self.image.clip_draw(0,0, 500,70, self.x, self.y+self.frame)