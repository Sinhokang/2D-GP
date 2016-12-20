import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image,Load,back
    image =load_image("./Resource/background/logo.png")
    Load =load_image("./Resource/background/event_detail_sample.png")
    back=load_image("./Resource/background/back.png")
    pass

def exit():
    global image,Load,back
    del(image)
    del(Load)
    del(back)


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
    pass

def draw(frame_time):
    clear_canvas()
    back.draw(400, 300)
    Load.draw(400,100)
    image.draw(400,300)
    
    update_canvas()
    pass




def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






