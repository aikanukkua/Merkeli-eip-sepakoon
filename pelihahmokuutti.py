import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Pelihahmokuutti")
x=50
y=50


def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.circle(naytto,(255,255,255),(400,350),50)
        pygame.draw.circle(naytto,(0,0,0),(380,330),10)
        pygame.draw.circle(naytto,(0,0,0),(420,330),10)

        pygame.draw.circle(naytto,(255,255,255),(360,380),17)
        pygame.draw.circle(naytto,(255,255,255),(440,380),17)
        pygame.draw.circle(naytto,(0,0,0),(390,370),12)
        pygame.draw.circle(naytto,(255,255,255),(385,360),10)
        pygame.draw.circle(naytto,(0,0,0),(410,370),12)
        pygame.draw.circle(naytto,(255,255,255),(415,360),10)
        pygame.draw.circle(naytto, (0, 0, 0), (400, 360), 7)
        pygame.display.flip()

main()