
import random

from pico2d import *
from Enemy import Monster



class Item_bomb:
    #monster=Monster()
    def __init__(self):
        self.x,self.y=50,100
        self.image=load_image('../Resource/object/item_bomb.png')


    def draw(self):
        self.image.draw(self.x,self.y)


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_z:
            self.update()



class Item_slow:
    def __init__(self):
        self.x, self.y = 750, 100
        self.image = load_image('../Resource/object/item_break.png')


    def draw(self):
        self.image.draw(self.x, self.y)

   # def handle_event(self, event):
      #  if event.type == SDL_KEYDOWN: