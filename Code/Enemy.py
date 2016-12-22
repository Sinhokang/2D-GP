import random
from pico2d import *

class Monster:

    PIXEL_PER_METER = (10.0/ 0.2)
    RUN_SPEED_KMPH = 10
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    image=None
    E_image=None

    def __init__(self):
        self.x, self.y = random.randint(350, 650),550
        self.by,self.by=400,400
        self.ey=500
        self.dir = 1
        self.dir2 = 1.5

        self.fall_speed = random.randint(150, 250)
        if Monster.image == None:
            self.image = load_image('./Resource/character/Enemy1.png')
        if Monster.E_image == None:
            self.E_image = load_image("./Resource/effect/hatzling_01_05.png")

    def update(self,frame_time):
        distance = Monster.RUN_SPEED_PPS * frame_time
        self.y -= (self.dir * distance)
        self.ey-=(self.dir2*distance)
        self.RUN_SPEED_PPS+=10
        if self.y <= -550:
            self.y = 550

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(0,0, 150,110, self.x, self.y)
        self.E_image.clip_draw(0,0,64,30,self.x,self.ey-40)

    def type(self, type):
        self.type = type
        if self.type == 1:
            self.image = load_image("./Resource/character/Enemy1.png")
        elif self.type == 2:
            self.image = load_image("./Resource/character/Enemy2.png")
        elif self.type == 3:
            self.image = load_image("./Resource/character/Enemy3.png")
        elif self.type == 4:
            self.image = load_image("./Resource/character/Enemy4.png")

    def get_bb(self):
        return self.x-22,self.y-25,self.x+22,self.y+25
    def get_aa(self):
        return self.x - 10, self.ey - 30, self.x + 10, self.ey -20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_aa())
