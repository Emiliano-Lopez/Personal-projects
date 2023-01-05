import pygame,sys
from tnt import Tnt





def spawn_tnt(settings,screen,sprites,time):
#    print( time-settings.tnt_spawn_delay)
    pass   



def check_events(car):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.moving_right = True

            if event.key == pygame.K_LEFT:
                car.moving_left = True

            if event.key == pygame.K_UP:
                car.moving_up = True

            if event.key == pygame.K_DOWN:
                car.moving_down = True

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                car.moving_right = False
                
            elif event.key == pygame.K_LEFT:
                car.moving_left = False

            elif event.key == pygame.K_UP:
                car.moving_up = False

            elif event.key == pygame.K_DOWN:
                car.moving_down = False






def update_screen(settings,screen,car,sprites,scoreboard):

        # Redraw the screen during each pass through the loop.

        screen.fill((0,0,0))
        #set background image
        screen.blit(settings.bg,(0,0))
        
        car.blitme()
        sprites.draw(screen)
        scoreboard.show_score()
        sprites.update()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

