import random
import json
import os

from pico2d import *
import stage2
import game_framework
import title_state
from BackGround import Background

from Player import aircraft
from misile import Missile
from Enemy  import Monster
from boss import Boss
from Item import Item_bomb
from Item import Item_slow

import Ranking_state
name = "MainState"


font = None
backgrounds=None
Bos=None
Enemy_Missile=[]
missiles=[]
monsters=[]
Stage1_boss=[]
life=15
bossDown=True
def enter():
    global player,backgrounds,monsters,item_bomb,item_slow,missile,font,boss
    global state,Enemy_Missile
    font = load_font('ENCR10B.TTF', 30)
    player=aircraft()
    boss=Boss()
    backgrounds=Background()
    monsters = create_monster()
    item_bomb=Item_bomb()
    item_slow=Item_slow()
    game_framework.reset_time()
    pass


def exit():

    global player,backgrounds,monster,item_bomb,item_slow,missile,font
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()
    score_data.append({"Time": player.life_time})
    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()
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
'''
def create_boss():
    create=[]
    boss=Boss()
    boss.set_pos(400,400)
    create.append(boss)
'''



def create_monster():
    create = []
    empty=[]
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
    global boss
    global Enemy_Missile
    global backgrounds
    global life
    global Stage1_boss
    global bossDown

    handle_events(frame_time)
    player.update(frame_time)
    backgrounds.update(frame_time)
    boss.update(frame_time)


    for monster in monsters:
        monster.update(frame_time)

    for missile in missiles:
        missile.update(frame_time)

    for missile in missiles:
        for monster in monsters:
            if collide(monster, missile):
                missiles.remove(missile)
                monsters.remove(monster)
                player.destroy(monster)
    if(bossDown==True):
        for missile in missiles:
            if collide(boss, missile):
                missiles.remove(missile)
                life -=1
                print(life)
                if(life==0):
                    bossDown=False


    '''
    for missile in missiles:
        for Boss in boss:
            if collide(Boss,missile):
                print(life)
                life-=1
                if(life==0):
                    Bos.remove(Boss)
    '''
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


    if(bossDown==True):
        boss.draw()


    #backgrounds.draw_bb()
    item_bomb.draw()
    item_slow.draw()

    update_canvas()



    delay(0.02)
    pass





