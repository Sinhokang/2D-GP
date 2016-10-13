import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class BackGround:
    def __init__(self):
        self.image = load_image('C:/DragonFlight/Resource/background/01.png')
        self.image2=load_image('C:/DragonFlight/Resource/background/01.png')
        self.frame=0

    def update(self):
        self.frame -= 0.3
        if self.frame <= -450:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(0, 0, 800, 600, 400, 300+self.frame)
        self.image.clip_draw(0, 0, 800, 550, 400, 800+self.frame)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('C:/DragonFlight/Resource/character/DragonSet.png')
        self.dir = 1

    def update(self):

        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(0, 0, 200,100, self.x, self.y)


def enter():
    global boy,background
    boy=Boy()
    background=BackGround()
    pass


def exit():
    global boy,background
    del(boy)
    del(background)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass


def update():
    boy.update()
    background.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    boy.draw()
    update_canvas()
    pass





