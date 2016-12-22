import random

from pico2d import *

class Missile:
    PIXEL_PER_METER = (20.0 / 1)
    RUN_SPEED_KMPH = 250
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y + 75
        self.dir = 1
        if Missile.image==None:
            self.image = load_image("./Resource/effect/Black_boost_02.png")

    def update(self, frame_time):
        distance = Missile.RUN_SPEED_PPS * frame_time
        self.y += (self.dir * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 25, self.x + 15, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


