import pygame
from pygame.sprite import Sprite
import random

class Tnt(Sprite):
    
    def __init__(self,screen,settings):
        super().__init__()

        self.screen= screen
        self.settings = settings
        

        self.image = pygame.image.load('images/tnt.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = random.randint(0,settings.screen_width-self.rect.right)
        self.rect.y = 0

        self.x_position = float(self.rect.x)
        self.y_postion = float(self.rect.y)

    def update(self):
        self.y_postion += self.settings.tnt_speed_factor
        self.rect.y = self.y_postion

        if self.rect.bottom == self.settings.screen_height+64:
            self.kill()
            self.settings.score += 1 

        if self.settings.tnt_speed_factor != 3:
            if self.settings.score % 5: 
                self.settings.tnt_speed_factor += 0.5



