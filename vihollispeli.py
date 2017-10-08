import pygame
import random

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Vihollispeli")

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 200, 50))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset):
    päähahmo = hahmot[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo[1]+=10
        elif tapahtuma.key == pygame.K_LEFT:
                päähahmo[1]-=10
        elif tapahtuma.key == pygame.K_UP:
            päähahmo[2]-=10
        elif tapahtuma.key == pygame.K_DOWN:
                päähahmo[2]+=10
    for vihollinen in viholliset:
        if vihollinen[1]<=640:
            vihollinen[1]+=1
        if vihollinen[1]>640:
            vihollinen[1]=0
            vihollinen[2] = random.randint(0, 400)


def main():
    kuuttihahmo = ["kuutti.jpg", 10, 10, False]
    merkel1 = ["angela.jpg", 340, 10, False]
    merkel2 = ["angela.jpg", 20, 144, False]
    merkel3 = ["angela.jpg", 150, 300, False]
    hahmot = [kuuttihahmo]
    viholliset = [merkel1, merkel2, merkel3]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset)

main()

