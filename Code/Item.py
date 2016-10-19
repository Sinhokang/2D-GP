










import random

from pico2d import *




class Item_bomb:
    def __init__(self):
        self.x,self.y=50,100
        self.image=load_image('../Resource/object/item_bomb.png')

    def draw(self):
        self.image.clip_draw(0,0,128,128,self.x,self.y)
   # def update(self):
     #   self.x+=0


class Item_slow:
    def __init__(self):
        self.x, self.y = 750, 100
        self.image = load_image('../Resource/object/item_break.png')

    def draw(self):
        self.image.clip_draw(0, 0, 128, 128, self.x, self.y)
