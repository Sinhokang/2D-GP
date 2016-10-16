import random

from pico2d import *



class Character:

    Lfly=True
    Rfly=True
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.image = load_image('../Resource/character/Player2.png')
        self.move=0

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.Lfly == False:
            self.x=max(150,self.x-15)
        elif self.Rfly==False:
            self.x=min(650,self.x+15)

        delay(0.01)


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




