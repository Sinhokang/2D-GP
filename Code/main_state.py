import random
import json
import os

from pico2d import *

import game_framework
import title_state
from BackGround import Background
from Player import Character
from Enemy  import Monster
from Player import Item_bomb
from Player import Item_slow

name = "MainState"

boy = None
grass = None
font = None
background=None
monster=None

def enter():
    global character,background,monster,item_bomb,item_slow
    character=Character()
    background=Background()
    monster=Monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()
    pass


def exit():
    global character,background,monster,item_bomb,item_slow
    del(character)
    del(background)
    del(monster)
    del(item_bomb)
    del(item_slow)
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
    monster.update()
    character.update()
    background.update()
   # item_bomb.update()
   # item_slow.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    character.draw()
    monster.draw()
    item_bomb.draw()
    item_slow.draw()
    update_canvas()
    delay(0.03)
    pass





