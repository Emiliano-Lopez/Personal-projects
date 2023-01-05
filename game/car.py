import pygame


class Car():

    def __init__(self, screen,settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.settings = settings
        # Load the ship image and get its rect.
        

        self.image = pygame.image.load('images/car_up.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        # update car position
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.car_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.car_speed_factor

        if self.moving_up and self.rect.top >0:
            self.bottom -= self.settings.car_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.settings.car_speed_factor
        
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
