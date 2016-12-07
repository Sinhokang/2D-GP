import random

from pico2d import *
#from BackGround import Background



class Monster:

    PIXEL_PER_METER = (10.0/ 0.2)
    RUN_SPEED_KMPH = 20
    '''
    if background.state==background.One:
        RUN_SPEED_KMPH = 0.5
    elif background.state==background.Two:
        RUN_SPEED_KMPH = 1.0
    elif background.state == background.Two:
        RUN_SPEED_KMPH=1.5
    elif background.state == background.Four:
        RUN_SPEED_KMPH=2.0
    '''
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.x, self.y = random.randint(350, 650),550
        self.dir = 1
        self.fall_speed = random.randint(150, 250)
        self.state=1

        self.image = load_image('../Resource/character/Enemy4.png')


    def update(self,frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.y -= (self.dir * distance)
        self.state=(self.state+1)%4
        if self.y <= -550:
            self.y = 550


    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0,0, 130,90, self.x, self.y)


    def get_bb(self):
        return self.x-22,self.y-25,self.x+22,self.y+25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())