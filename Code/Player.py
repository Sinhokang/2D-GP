import random
import json
import os
from pico2d import *



class aircraft:

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 50.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image =None
    Lfly=True
    Rfly=True
    destroy_sound=None
    hit_sound=None
    die_sound=None
    playerdeath_sound=None
    thunder_sound=None
    thunder2_sound = None
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.life_time = 0.0
        self.dir = 1
        if aircraft.image==None:
            self.image = load_image('./Resource/character/Player2.png')
        if aircraft.destroy_sound==None:
            aircraft.destroy_sound=load_wav('./Resource/sound/ch_die.wav')
            aircraft.destroy_sound.set_volume(65)
        if aircraft.hit_sound == None:
            aircraft.hit_sound = load_wav('./Resource/sound/dragon_breathe.wav')
            aircraft.hit_sound.set_volume(45)
        if aircraft.die_sound == None:
            aircraft.die_sound = load_wav('./Resource/sound/dragon_death.wav')
            aircraft.die_sound.set_volume(100)
        if aircraft.playerdeath_sound == None:
            aircraft.playerdeath_sound = load_wav('./Resource/sound/thrown_projectile_hit_01.wav')
            aircraft.playerdeath_sound.set_volume(100)
        if aircraft.thunder_sound==None:
            aircraft.thunder_sound= load_wav('./Resource/sound/thunder.wav')
            aircraft.thunder_sound.set_volume(50)

       # if aircraft.thunder2_sound == None:
        #    aircraft.thunder2_sound = load_wav('./Resource/sound/alert.wav')
         #   aircraft.thunder2_sound.set_volume(60)

    def die(self, boss):
        self.die_sound.play()
    def hit(self, boss):
        self.hit_sound.play()

    def destroy(self,monster):
        self.destroy_sound.play()
    def playerdeath(self,playr):
        self.playerdeath_sound.play()
    def thunder(self,thun):
        self.thunder_sound.play()
#    def thunder2(self,thun):
 #       self.thunder2_sound.play()
    def update(self,frame_time):
        distance = aircraft.RUN_SPEED_PPS * frame_time
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.life_time += frame_time
        self.frame = (self.frame + 1) % 8




        if self.Lfly == False:
            self.x -= (self.dir * distance)
            self.x = clamp(150, self.x, 650)
        elif self.Rfly==False:
            self.x += (self.dir * distance)
            self.x = clamp(150, self.x, 650)



    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 90, 100, self.x, self.y)



    def handle_event(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.Rfly = False
            if event.key == SDLK_LEFT:
                self.Lfly = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.Rfly = True
            elif event.key == SDLK_LEFT:
                self.Lfly = True


    def get_bb(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 40

    def get_aa(self):
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
