import pygame
import time 

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf')
width = 900
height = 800
screen = pygame.display.set_mode([width, height])
bgs = []
banners = []
level = 1
menu_img = pygame.image.load(f'meu_deus_me_ajuda_porfavor/imagens/1.png')


for i in range(1,4):
    bgs.append(pygame.image.load(f'meu_deus_me_ajuda_porfavor/imagens/{i}.png'))
    
run = True
while run:
    timer.tick(fps)
    
    screen.fill('black')
    screen.blit(bgs[level - 1] (0,0))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
        
    pygame.display.flip()
pygame.quit()





























