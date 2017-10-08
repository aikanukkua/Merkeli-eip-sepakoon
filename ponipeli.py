import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Ponipeli")

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))



def piirtaminen(naytto, hahmot):
    naytto.fill((0, 200, 50))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma):
    if tapahtuma.type == pygame.KEYDOWN:
        päähahmo=hahmot[0]
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo[1]+=10
        elif tapahtuma.key == pygame.K_LEFT:
                päähahmo[1]-=10
        elif tapahtuma.key == pygame.K_UP:
            päähahmo[2]-=10
        elif tapahtuma.key == pygame.K_DOWN:
                päähahmo[2]+=10



def poninKeskipiste(hahmot):
    päähahmo = hahmot[0]
    poninKeskipiste = [(päähahmo[1]+112), (päähahmo[2]+78)]
    print(poninKeskipiste)
    return poninKeskipiste

def asetaJalkapallo(hahmot, ebinReturni):
    pallojeejee = hahmot[1]
    pallojeejee[1] = ebinReturni[0]-37
    pallojeejee[2] = ebinReturni[1]-26

def main():
    poni = ["poni.jpg", 10, 10, False]
    jalkapallo = ["jalkapallo.jpg", 10, 10, False]
    hahmot = [poni,jalkapallo]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        ebinReturni = poninKeskipiste(hahmot)
        kontrolli(hahmot, tapahtuma)
        piirtaminen(naytto, hahmot)
        asetaJalkapallo(hahmot, ebinReturni)



main()