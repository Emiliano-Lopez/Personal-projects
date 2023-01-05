import pygame


class Settings():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 700
        self.bg = pygame.image.load("images/road.png")
        self.font =  ["comic sans", 50]

        self.aux_time = 1
        self.car_speed_factor = 2

        self.tnt_speed_factor = 1.5
        self.tnt_spawn_delay = 0
        self.score = 0