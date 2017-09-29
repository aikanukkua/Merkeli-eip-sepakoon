import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Merkeliäeipääsepakoon")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot):
    naytto.fill((0, 255, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma):
    päähahmo = hahmot[1]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            if päähahmo[1]<350:
                päähahmo[1]+=10
        elif tapahtuma.key == pygame.K_LEFT:
            if päähahmo[1]>50:
                päähahmo[1]-=10
        elif tapahtuma.key == pygame.K_UP:
            if päähahmo[2]>10:
                päähahmo[2]-=10
        elif tapahtuma.key == pygame.K_DOWN:
            if päähahmo[2]<350:
                päähahmo[2]+=10

def main():
    kuuttihahmo = ["kuutti.jpg", 10, 10, False]
    angelahahmo = ["angela.jpg", 340, 10, False]
    hahmot = [angelahahmo, kuuttihahmo]
    while True:

        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma)
        piirtaminen(naytto, hahmot)


main()
