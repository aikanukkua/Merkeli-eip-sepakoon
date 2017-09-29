import pygame
import random
import time

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("satunnainensijainti")
naytto.fill((0, 0, 0))
x=random.randint(1,640)
y=random.randint(1,400)

def piirraKuva(piirraKuva):
    while True:
        kuva = pygame.image.load(piirraKuva).convert()
        naytto.blit(kuva, (x,y))
        pygame.display.flip()
        time.sleep(3)
        if piirraKuva.type == pygame.QUIT:
            break


piirraKuva("angela.jpg")