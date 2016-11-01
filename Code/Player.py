import random

from pico2d import *



class Player_Character:
    '''
    PIXEL_PER_METER = (1.0 / 0.03)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    '''
    Lfly=True
    Rfly=True


    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('../Resource/character/Player2.png')
        self.move=0
        self.dir =1

    def update(self):
        self.frame = (self.frame + 1) % 8
        #distance=Player_Character.RUN_SPEED_PPS*frame_time
        #self.x+=(self.dir*distance)

        if self.Lfly == False:
            self.x=max(150,self.x-15)
        elif self.Rfly==False:
            self.x=min(650,self.x+15)





    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 100, self.x, self.y)

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




class Missile:
    image=None

    def __init__(self,x,y):
        self.x,self.y= x,y+75
        self.image= load_image("../Resource/effect/Black_boost_02.png")

    def update(self):
        self.y +=25

    def draw(self):
        self.image.draw(self.x,self.y)



