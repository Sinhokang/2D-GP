import random

from pico2d import *



class Character:

    Lfly=True
    Rfly=True
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('../Resource/character/Player2.png')
        self.dir = 1
        self.move=0

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.Lfly == False:
            self.move-=10
        elif self.Rfly==False:
            self.move+=10

        delay(0.01)


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 100, self.x+self.move, self.y)

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



'''
class Enemy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('../Resource/character/Player2.png')
        self.dir = 1

    def update(self):
        self.frame=(self.frame+1)%8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1
        delay(0.01)
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 90,100, self.x, self.y)

'''