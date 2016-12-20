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
        self.x,self.y=400,500
        self.bossUP=True
        self.life=15
        self.dir=1
        if Boss.image == None:
            self.image = load_image('./Resource/character/Boss2.png')


    def update(self,frame_time):
        distance = Boss.RUN_SPEED_PPS * frame_time
        self.y -= (self.dir * distance)

        if self.y <=450:
            self.y=450


        '''
        self.rate+=1
        print(self.rate)
        if(self.rate>100):
            self.bossUP=False
        '''
    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0, 0, 500, 400, self.x, self.y)

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 200

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




