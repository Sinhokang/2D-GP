import random
import json
import os
from pico2d import *



class Player_Character:

    PIXEL_PER_METER = (20.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    Lfly=True
    Rfly=True
    global font

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.image = load_image('../Resource/character/Player2.png')
        self.move=0
        self.dir =1
        font = load_font('ENCR10B.TTF', 40)
       # LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def update(self,frame_time):
        self.life_time += frame_time
        self.frame = (self.frame + 1) % 8
        distance=Player_Character.RUN_SPEED_PPS*frame_time
        #self.x+=(self.dir*distance)

        if self.Lfly == False:
            self.x=max(150,self.x-15)
        elif self.Rfly==False:
            self.x=min(650,self.x+15)
      #  font.draw(500, 450, 'Time:%4.1f' % (self.life_time), (0, 0, 0))
    '''
    def update(self,frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Player_Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Player_Character.FRAMES_PER_ACTION * Player_Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.dir * distance)

        self.x = clamp(150, self.x, 650)
    '''



    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 100, self.x, self.y)


    '''
    def handle_event(self,event):
        def handle_event(self, event):
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                    self.state = self.LEFT_RUN
                    self.dir = -1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                    self.state = self.RIGHT_RUN
                    self.dir = 1
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
                    self.dir = 0
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
                    self.dir = 0

        '''
    def handle_event(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.Rfly = False
                print('gg')
            if event.key == SDLK_LEFT:
                self.Lfly = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.Rfly = True
            elif event.key == SDLK_LEFT:
                self.Lfly = True


    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Missile:

    image=None

    def __init__(self,x,y):
        self.x,self.y= x,y+75
        self.image= load_image("../Resource/effect/Black_boost_02.png")

    def update(self):
        self.y +=25

    def draw(self):
        self.image.draw(self.x,self.y)



