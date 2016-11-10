import random

from pico2d import *
from BackGround import Background



class Monster:


    PIXEL_PER_METER = (1000.0/ 0.3)
    RUN_SPEED_KMPH = 0.5
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.x, self.y = random.randint(350, 650), 550
        self.dir = 1
        self.fall_speed = random.randint(90, 170)
        self.state=0

        self.image = load_image('../Resource/character/Enemy4.png')


    def update(self,frame_time):
        self.y -= frame_time * self.fall_speed
        '''
        if Background.state==1:
            dir=1
        elif Background.state==2:
            dir=1.5
        elif Background.state==3:
            dir=2
        elif Background.state==4:
            dir=2.5
        '''
        print(self.y)
        if self.y <= -550:
            self.y = 550
        print("가능?")

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0,0, 100,70, self.x, self.y)


    def get_bb(self):
        return self.x-22,self.y-25,self.x+22,self.y+25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())