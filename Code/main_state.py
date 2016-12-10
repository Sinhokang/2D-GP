import random
import json
import os

from pico2d import *

import game_framework
import title_state
from BackGround import Background

from Player import aircraft
from misile import Missile
from Enemy  import Monster

from Item import Item_bomb
from Item import Item_slow

import Ranking_state
name = "MainState"


grass = None
font = None
backgrounds=None
boss=None
Enemy_Missile=[]
missiles=[]
monsters=[]
bosss=[]

def enter():
    global player,backgrounds,monsters,item_bomb,item_slow,missile,font
    global state,Enemy_Missile
    font = load_font('ENCR10B.TTF', 30)
    player=aircraft()
    backgrounds=Background()
    monsters = create_monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()
    game_framework.reset_time()
    pass


def exit():

    global player,backgrounds,monster,item_bomb,item_slow,missile,font,boss
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()
    score_data.append({"Time": player.life_time})
    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()
    del(font)
    del(player)
    del(backgrounds)
    del(monster)
    del(item_bomb)
    del(item_slow)
    del(boss)
    #del(missile)

    pass


def pause():
    pass


def resume():
    pass


def collide(a,b):

    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()


    if left_a>right_b : return False
    if right_a<left_b : return False
    if top_a<bottom_b : return False
    if bottom_a>top_b : return False

    return True


def collide2(a, b):
    left_a, bottom_a, right_a, top_a = a.get_aa()
    left_b, bottom_b, right_b, top_b = b.get_aa()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def handle_events(frame_time):

    global missiles
    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            game_framework.change_state(Ranking_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            newmisslies = Missile(player.x,player.y)
            missiles.append(newmisslies)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            item_bomb.handle_event(event)
            for monster in monsters:
                monsters.remove(monster)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            item_slow.handle_event(event)
        else:
            player.handle_event(event)



    pass



def create_monster():
    create = []

    monster1 = Monster()
    monster1.set_pos(35 * 5, 550)
    monster1.type(random.randint(1, 5))
    create.append(monster1)

    monster2 = Monster()
    monster2.set_pos(35 * 9, 550)
    monster2.type(random.randint(1, 5))
    create.append(monster2)

    monster3 = Monster()
    monster3.set_pos(35 * 12, 550)
    monster3.type(random.randint(1, 5))
    create.append(monster3)

    monster4 = Monster()
    monster4.set_pos(35 * 15, 550)
    monster4.type(random.randint(1, 5))
    create.append(monster4)

    monster5 = Monster()
    monster5.set_pos(35 * 19, 550)
    monster5.type(random.randint(1, 5))
    create.append(monster5)

    monster6 = Monster()
    monster6.set_pos(35 * 30, 550)
    create.append(monster6)

    return create

def update(frame_time):


    global monsters
    global missiles
    global bosss
    global Enemy_Missile
    global backgrounds
    handle_events(frame_time)
    player.update(frame_time)
    backgrounds.update(frame_time)
    for monster in monsters:
        monster.update(frame_time)


    for missile in missiles:
        missile.update(frame_time)

    for missile in missiles:
        for monster in monsters:
            if collide(monster, missile):
                missiles.remove(missile)
                monsters.remove(monster)

    for missile in missiles:
        for background in backgrounds:
            if collide(background, missile):
                missiles.remove(missile)
                backgrounds.remove(background)
                #for missile in missiles:
   

    for monster in monsters:
        if collide(monster, player) :
            game_framework.push_state(Ranking_state)
    for monster in monsters:
        if collide2(monster, player):
            game_framework.push_state(Ranking_state)


    for monster in monsters:
        if monster.y <= -20:
            monsters = create_monster()
        elif monster==[]:
            create_monster()

    #monster.update(frame_time)


    #(player.life_time)
    #font.draw(100, 450 - 40 * i, 'TIME:%4.1f'
           #   % (score['Time']), (100, 150, 150))


def draw(frame_time):
    clear_canvas()
    backgrounds.draw()
    player.draw()
    player.draw_bb()
    #background.get_bb()
    font.draw(600, 550, 'Time:%4.1f' % (player.life_time), (255, 255, 255))
    for missile in missiles:
        missile.draw()
    for missile in missiles:
        missile.draw_bb()

    for monster in monsters:
        monster.draw()
    for monster in monsters:
        monster.draw_bb()

    backgrounds.draw_bb()
    item_bomb.draw()
    item_slow.draw()

    update_canvas()



    delay(0.02)
    pass





