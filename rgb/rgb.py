import pygame
from sys import exit

pygame.init()

larg = 400
alt = 600

tela = pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Tela RGB.py")

font = pygame.font.SysFont('Arial', 15, True, True)

cores = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (250, 240, 230), (255, 192, 203),
         (255, 20, 147), (199, 21, 133), (30, 144, 255), (124, 252, 0), (0, 255, 255), (64, 224, 208), (0, 0, 139),
         (20, 20, 20), (25, 25, 0), (50, 40, 230), (25, 92, 23), (55, 20, 14), (19, 21, 33), (30, 44, 25),
         (124, 25, 0), (0, 25, 25), (64, 24, 8), (0, 0, 19), (0, 0, 0)]

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

active = True


def muda_cor(tmp=90):
    """

    :param tmp: valor do delay entre as cores
    :return: null
    """
    p = 0
    for c in cores:
        tela.fill(cores[p])
        pygame.time.delay(tmp)

        for l in letras:
            msg = f'{letras[p]}'
            tam = font.render(msg, True, cores[-1])
            tela.blit(tam, (larg / 2, alt / 2))

        p += 1
        if p == len(cores):
            p = 0
        pygame.display.update()


while active:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    muda_cor(250)

    pygame.display.update()
