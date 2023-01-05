import pygame

pygame.init()
aux=0
while True:
    
    tiempo=pygame.time.get_ticks()/1000
 
    if tiempo-aux > 5:
        aux=tiempo
        print(aux-tiempo)
        break
        
