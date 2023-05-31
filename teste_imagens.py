import pygame
import math

pygame.init()
largura = 1600
altura = 1300
timer = pygame.time.Clock()
screen = pygame.display.set_mode([largura,altura])
caixa = []
bgs = []
level = 1


for i in range (1,7):
    bgs.append(pygame.image.load(f'meu_deus_me_ajuda_porfavor/imagens/{i}.png'))
    caixa.append(pygame.image.load(f'meu_deus_me_ajuda_porfavor/imagens/Questões.png'))


run = True
while run:
    timer.tick
    screen.fill('black')
    screen.blit(bgs[level - 1], (0,0))
    screen.blit(caixa[level - 1]), (largura/2, altura/2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.flip()
pygame.quit()
    
    