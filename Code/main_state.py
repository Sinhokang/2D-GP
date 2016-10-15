import random
import json
import os

from pico2d import *

import game_framework
import title_state
from BackGround import Background
from Player import Character

name = "MainState"

boy = None
grass = None
font = None
background=None
'''
class BackGround:
    def __init__(self):
        self.image = load_image('C:/DragonFlight/Resource/background/01.png')
        self.image2=load_image('C:/DragonFlight/Resource/background/01.png')
        self.frame=0

    def update(self):
        self.frame -= 2.0
        if self.frame <= -600:
            self.frame = 0

    def draw(self):
        #self.image.clip_draw(0, 0, 800, 600, 400, 600 + self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 100+self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 700+self.frame)
        self.image.clip_draw(0, 0, 800, 600, 400, 1300 + self.frame)
'''
'''
class Boy:
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

def enter():
    global character,background
    character=Character()
    background=Background()

    pass


def exit():
    global character,background
    del(character)
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
        else:
           character.handle_event(event)
        '''
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                Rfly = False
                print('gg')
            if event.key == SDLK_LEFT:
                Lfly = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Rfly= True
            elif event.key == SDLK_LEFT:
                Lfly = True

    '''
    pass


def update():

    handle_events()
    character.update()
    background.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    character.draw()
    update_canvas()

    pass





