import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Ensimmäinen peli")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 0, 255), (1, 1), (640, 400))
        pygame.draw.line(naytto, (0,255,0), (1,400), (640,1))
        pygame.display.flip()

main()