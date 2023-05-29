#Testar no main


import pygame

#medidas da janela                     ------------------- OLhar o minuto final do video para entender comoutilizar isto como uma class em outros arquivos------------------------------
janela_altura = 1000
janela_largura = 707


janela = pygame.display.set_mode((janela_largura,janela_altura))

pygame.display.set_caption('teste na aba')

menu_image = pygame.image.load('imagem/0.png').convert_alpha()

#classe dos botões
class Button1():
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.clicked = False
    def verificar_clique(self,):
        action = False
        #pegando a posição do mouse
        pos = pygame.mouse.get_pos()
        pos_x,pos_y = pos
        if self.x - (self.largura/2) <= pos_x <= self.x + (self.largura/2) and self.y - (self.altura/2) <= pos_y <= self.y + (self.altura/2):
            
         if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
             self.clicked = True
             action = True
       
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        return action
#game  loop
run = True
while run:
    janela.fill((200,228,241))
   
   
   #Apenas mostrando como seia possivel dar funcionalidades aos botões criados 
    #if  start_button.draw():
      #  print ('start')
   # if exit_button.draw():
      #  run = False
      #  print("EXIT")
    
    #event handler(le os eventos do jogo aparentemente)
    for envent in pygame.event.get():
        #sair do jogo
        if envent.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()