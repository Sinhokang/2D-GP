
import game_framework
import main_state
from pico2d import *
import Ranking_state

name = "TitleState"
image = None


def enter():
    global image,bgm
    bgm = load_music('./Resource/sound/bgm_lobby.ogg')
    bgm.set_volume(64)
    bgm.repeat_play()
    image =load_image("./Resource/background/start.png")
    #Load =load_image("./Resource/background/event_detail_sample.png")
    #back=load_image("./Resource/background/back.png")
    pass

def exit():
    global image
    del(image)
    #del(Load)
    #del(back)


def handle_events(frame_time):
    events =get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
                game_framework.change_state(Ranking_state)
            elif event.type==SDL_MOUSEBUTTONDOWN:
                x,y=event.x,600-event.y
                print(x,y)
                if(x>245 and x<535 and y>123 and y<183 ):
                    game_framework.change_state(main_state)
                if (x > 245 and x < 535 and y > 24 and y < 83):
                    game_framework.change_state(Ranking_state)

    pass

def draw(frame_time):
    clear_canvas()
    show_cursor()
    image.draw(400,300)

    update_canvas()
    pass




def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






