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

import Ranking_state
name = "MainState"

boy = None
grass = None
font = None
background=None
boss=None
missiles=[]
monsters=[]
bosss=[]

def enter():
    global player,background,monsters,item_bomb,item_slow,missile,font

    font = load_font('ENCR10B.TTF', 40)
    player=Player_Character()
    background=Background()
    monsters = create_monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()
    game_framework.reset_time()


    pass


def exit():

    global player,background,monster,item_bomb,item_slow,missile,font,boss
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()
    score_data.append({"Time": player.life_time})
    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()
    del(font)
    del(player)
    del(background)
   # del(monster)
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            item_slow.handle_event(event)
        else:
            player.handle_event(event)



    pass



def create_monster():
    global state
    state=0
    state=(state+1)%4
    create = []
    if(state ==1):
        #monster1 = Monster()
        #monster1.set_pos(35 * 5, 550)
        #create.append(monster1)

        monster3 = Monster()
        monster3.set_pos(35 * 15, 550)
        create.append(monster3)

        monster5 = Monster()
        monster5.set_pos(35 * 13, 550)
        create.append(monster5)

        monster7 = Monster()
        monster7.set_pos(35 * 17, 550)
        create.append(monster7)

        #monster10 = Monster()
        #monster10.set_pos(35 * 7, 550)
        #create.append(monster10)

        monster9 = Monster()
        monster9.set_pos(35 * 30, 550)
        create.append(monster9)

    elif state ==2:
        monster2 = Monster()
        monster2.set_pos(35 * 5, 550)
        create.append(monster2)

        monster4 = Monster()
        monster4.set_pos(35 * 11, 550)
        create.append(monster4)

        monster6 = Monster()
        monster6.set_pos(35 * 15, 550)
        create.append(monster6)

        monster7 = Monster()
        monster7.set_pos(35 * 17, 550)
        create.append(monster7)

        monster8 = Monster()
        monster8.set_pos(35 * 19, 550)
        create.append(monster8)

        monster9 = Monster()
        monster9.set_pos(35 * 30, 550)
        create.append(monster9)

    elif state==3:
        monster1 = Monster()
        monster1.set_pos(35 * 3, 550)
        create.append(monster1)

        monster2 = Monster()
        monster2.set_pos(35 * 5, 550)
        create.append(monster2)

        monster5 = Monster()
        monster5.set_pos(35 * 13, 550)
        create.append(monster5)

        monster6 = Monster()
        monster6.set_pos(35 * 15, 550)
        create.append(monster6)

        monster8 = Monster()
        monster8.set_pos(35 * 19, 550)
        create.append(monster8)

        monster9 = Monster()
        monster9.set_pos(35 * 30, 550)
        create.append(monster9)

    elif state ==4:
        monster1 = Monster()
        monster1.set_pos(35 * 3, 550)
        create.append(monster1)

        monster3 = Monster()
        monster3.set_pos(35 * 7, 550)
        create.append(monster3)

        monster4 = Monster()
        monster4.set_pos(35 * 11, 550)
        create.append(monster4)

        monster7 = Monster()
        monster7.set_pos(35 * 17, 550)
        create.append(monster7)

        monster8 = Monster()
        monster8.set_pos(35 * 19, 550)
        create.append(monster8)

        monster9 = Monster()
        monster9.set_pos(35 * 30, 550)
        create.append(monster9)


   # if team()==0:
      #  create_monster_team()
    return create

def update(frame_time):
    appear=True
    dis=4
    global monsters
    global missiles
    global bosss
    handle_events(frame_time)
    for monster in monsters:
        monster.update(frame_time)

    for missile in missiles:
        missile.update(frame_time)

    for missile in missiles:
        for monster in monsters:
            if collide(monster, missile):
                missiles.remove(missile)
                monsters.remove(monster)

    #for missile in missiles:
      #  for boss in bosss:
     #       if collide(boss, missile):
      #          missiles.remove(missile)
       #         dis-=1
        #        print(dis)
         #       if(dis==0):
          #          bosss.remove(boss)

    for monster in monsters:
        if collide(monster, player):
            game_framework.push_state(Ranking_state)

    for monster in monsters:
        if monster.y <= -20:
            monsters = create_monster()

    #monster.update(frame_time)
    player.update(frame_time)
    background.update()
    font.draw(500,450,'Time:%4.1f'%(player.life_time),(0,0,0))
    print(player.life_time)
    #font.draw(100, 450 - 40 * i, 'TIME:%4.1f'
           #   % (score['Time']), (100, 150, 150))


def draw(frame_time):
    clear_canvas()
    background.draw()
    player.draw()
    player.draw_bb()
    #background.get_bb()

    for missile in missiles:
        missile.draw()
    for missile in missiles:
        missile.draw_bb()

    for monster in monsters:
        monster.draw()
    for monster in monsters:
        monster.draw_bb()

    item_bomb.draw()
    item_slow.draw()

    update_canvas()



    delay(0.02)
    pass





