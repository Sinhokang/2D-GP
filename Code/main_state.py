import random
import json
import os

from pico2d import *

import game_framework
import title_state
from BackGround import Background
from Player import Player_Character
from Player import Missile
from Enemy  import Monster
from Item import Item_bomb
from Item import Item_slow

name = "MainState"

boy = None
grass = None
font = None
background=None
monster=None
missiles=[]

def enter():
    global player,background,monster,item_bomb,item_slow,missile
    player=Player_Character()
    background=Background()
    monster=Monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()

    pass


def exit():
    global player,background,monster,item_bomb,item_slow,missile
    del(player)
    del(background)
    del(monster)
    del(item_bomb)
    del(item_slow)
    #del(missile)

    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global missiles
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            newmisslies = Missile(player.x,player.y)
            missiles.append(newmisslies)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            item_bomb.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            item_slow.handle_event(event)
        else:
            player.handle_event(event)



    pass


def update():
    handle_events()
    for missile in missiles:
        missile.update()
    monster.update()
    player.update()
    background.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    monster.draw()
    item_bomb.draw()
    item_slow.draw()
    for missile in missiles:
        missile.draw()
    update_canvas()
    delay(0.03)
    pass





