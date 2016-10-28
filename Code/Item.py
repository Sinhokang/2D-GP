
import random

from pico2d import *
from Enemy import Monster



class Item_bomb:
    #monster=Monster()
    def __init__(self):
        self.x,self.y=50,100
        self.nx,self.ny=50,150
        self.frame=0
        self.image=load_image('../Resource/object/item_bomb.png')
        self.Num=load_image('../Resource/ui/Number.png')

    def draw(self):
        self.image.draw(self.x,self.y)
        self.Num.clip_draw(self.frame*100,0,40,20,self.nx,self.ny)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_z:
            self.update()



class Item_slow:
    def __init__(self):
        self.x, self.y = 750, 100
        self.nx, self.ny = 750, 150
        self.frame=0
        self.image = load_image('../Resource/object/item_break.png')
        self.Num = load_image('../Resource/ui/Number.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        self.Num.clip_draw(self.frame * 100, 0, 40, 20, self.nx, self.ny)


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_x:
            self.update()
