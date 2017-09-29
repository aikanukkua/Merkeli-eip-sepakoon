import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Ensimmäinen peli")

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((255, 0, 0))
        pygame.draw.circle(naytto, (0, 255, 0), (220,100),100)
        pygame.display.flip()

main()
