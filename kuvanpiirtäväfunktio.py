import pygame
import time

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Kuvanpiirtäväfunktio")
x=50
y=50
naytto.fill((0, 0, 0))

def piirraKuva(piirraKuva):
    while True:
        kuva = pygame.image.load(piirraKuva).convert()
        naytto.blit(kuva, (x, y))
        pygame.display.flip()
        time.sleep(2)
        if piirraKuva.type == pygame.QUIT:
            break

piirraKuva("angela.jpg")