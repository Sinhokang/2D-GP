import random

from pico2d import *



class Background:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 0.3 m
    RUN_SPEED_KMPH = 30.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
   #100픽셀에 3미터 800*2400 2400M*7200M 크기의 종스크롤 방식
    one=None
    two=None
    three=None
    four=None
    One,Two,Three,Four=1,2,3,4

    def __init__(self):
        self.x, self.y = 400, 400
        if Background.one == None:
            self.one = load_image('./Resource/background/01.png')
        if Background.two == None:
            self.two=load_image('./Resource/background/02.png')
        if Background.three == None:
            self.three=load_image('./Resource/background/03.png')
        if Background.four == None:
            self.four = load_image('./Resource/background/04.png')
        self.bgm = load_music('./Resource/sound/music_maintheme.ogg')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.frame=0
        self.frame2=0
        self.frame3=0
        self.frame4=0
        self.state=self.One


    def update(self,frame_time):
        if self.state==self.One:
            self.frame -= 1.0#1
            if self.frame <= -600:
                self.frame = 0
                self.state=self.Two
        if self.state==self.Two:
            self.frame2 -= 2.0#2
            if self.frame2 <= -600:
                self.frame2=0
                self.state=self.Three
                self.y=0
        if self.state==self.Three:
            self.frame3 -= 3.0 #3
            if self.frame3 <= -600:
                self.frame3=0
                self.state=self.Four
                self.y=0
        if self.state==self.Four:
            self.frame4 -= 5.0
            if self.frame4 <= -2400:
                self.frame4=0
                self.state=self.One
                self.y=0



    def draw(self):
        if self.state==self.One:
            self.one.clip_draw(0, 0, 800, 600, 400, 100+self.frame)
            self.one.clip_draw(0, 0, 800, 600, 400, 700+self.frame)
            self.one.clip_draw(0, 0, 800, 600, 400, 1300 + self.frame)

        if self.state == self.Two:
            self.two.clip_draw(0, 0, 800, 600, 400, 100 + self.frame2)
            self.two.clip_draw(0, 0, 800, 600, 400, 700 + self.frame2)
            self.two.clip_draw(0, 0, 800, 600, 400, 1300 + self.frame2)
        if self.state == self.Three:
            self.three.clip_draw(0, 0, 800, 600, 400, 100 + self.frame3)
            self.three.clip_draw(0, 0, 800, 600, 400, 700 + self.frame3)
            self.three .clip_draw(0, 0, 800, 600, 400, 1300 + self.frame3)
        if self.state == self.Four:
            self.four.clip_draw(0, 0, 800, 600, 400, 100 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 700 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 1300 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 1900 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 2500 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 3100 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 3700 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 4300 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 4900 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 5500 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 6100 + self.frame4)
            self.four.clip_draw(0, 0, 800, 600, 400, 6700 + self.frame4)






