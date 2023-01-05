import pygame

class Scoreboard():

    def __init__(self, settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.position = self.screen_rect.topleft
        self.settings = settings
        
        self.textfont = pygame.font.SysFont(settings.font[0],settings.font[1])

        self.score_text = self.textfont.render("score: "+str(self.settings.score),1,(0,0,0))

    def update(self):
        self.score_text = self.textfont.render("score: "+str(self.settings.score),1,(0,0,0))



    def show_score(self):
        self.screen.blit(self.score_text,self.position)
