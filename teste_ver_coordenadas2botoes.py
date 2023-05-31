import pygame

height = 1000
widht = 707
screen = pygame.display.set_mode((widht,height))
run = True
tela = []
level = 21
tela = (pygame.image.load(f'imagem/{level}.png'))    #usar de base para verificar os diretórios
while run:
    screen.fill('black')
    screen.blit(tela,(0,0))
    pos = pygame.mouse.get_pos()
    print(pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
pygame.quit()
