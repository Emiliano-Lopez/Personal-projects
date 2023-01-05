import pygame
from pygame.sprite import Group
import sys
from settings import Settings
import game_functions as gf
from car import Car
from tnt import Tnt
from scoreboard import Scoreboard

def run():
    
    pygame.init()
    clock = pygame.time.Clock()
  

    settings= Settings()
    

    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    sprites = Group()
    car = Car(screen,settings)
    tnt = Tnt(screen,settings)
    scoreboard = Scoreboard(settings, screen)

    
    sprites.add(tnt)
    pygame.display.set_caption("car")
    time=pygame.time.get_ticks()/1000
    while True:
        gf.check_events(car)
        car.update()
        gf.spawn_tnt(settings,screen,sprites,time)

        if time-settings.tnt_spawn_delay == 2:
            tnt =Tnt(screen,settings)
            sprites.add(tnt)
            settings.tnt_spawm_delay = 0
        print(time-settings.tnt_spawn_delay)

        gf.update_screen(settings,screen,car,sprites,scoreboard)
        scoreboard.update()

        clock.tick()


run()
