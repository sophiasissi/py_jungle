import pygame
import math

pygame.init()
timer = pygame.time.Clock()
#medidas da janela                ------------------- OLhar o minuto final do video para entender como utilizar isto como uma class em outros arquivos(video dos botões)------------------------------
janela_altura = 1000
janela_largura = 707
global janela
janela = pygame.display.set_mode([janela_largura,janela_altura])
menu = []
fonte = pygame.font.Font('imagem/Fonte/myFont.ttf', 32)
fps = 60
screen = pygame.display.set_mode((janela_largura,janela_altura))
pygame.display.set_caption('teste na aba')
level = 0
pos = pygame.mouse.get_pos()
menu.append(pygame.image.load(f'imagem\Menus\{level}.png'))    #usar de base para verificar os diretórios

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    screen.blit(menu[level],(0,0))
    
    print(pos)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.flip()
pygame.quit()

