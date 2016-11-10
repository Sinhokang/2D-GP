import random

from pico2d import *





class Background:

    One,Two,Three,Four=1,2,3,4
    def __init__(self):
        self.one = load_image('../Resource/background/01.png')
        self.two=load_image('../Resource/background/02.png')
        self.three=load_image('../Resource/background/03.png')
        self.four = load_image('../Resource/background/04.png')
        self.frame=0
        self.frame2=0
        self.frame3=0
        self.frame4=0
        self.state=self.One

    def update(self):
        if self.state==self.One:
            self.frame -= 1.0
            if self.frame <= -600:
                self.frame = 0
                self.state=self.Two
        if self.state==self.Two:
            self.frame2 -= 2.0
            if self.frame2 <= -600:
                self.frame2=0
                self.state=self.Three
                self.y=0
        if self.state==self.Three:
            self.frame3 -= 3.0
            if self.frame3 <= -600:
                self.frame3=0
                self.state=self.Four
                self.y=0
        if self.state==self.Four:
            self.frame4 -= 5.0
            if self.frame4 <= -600:
                self.frame4=0
                self.state=self.One
                self.y=0

        #print (self.change)

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






