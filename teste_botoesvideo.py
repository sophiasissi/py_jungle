import pygame

#medidas da janela                     ------------------- OLhar o minuto final do video para entender comoutilizar isto como uma class em outros arquivos------------------------------
janela_altura = 2000
janela_largura = 1414

janela = pygame.display.set_mode((janela_largura,janela_altura))
pygame.display.set_caption('teste na aba')

menu_image = pygame.image.load('imagem/0.png').convert_alpha()

#classe dos botões
class Button1():
    def __init__(self,x,y,image):
        self.image = image
        self.caixa = self.image.get_rect()
        self.caixa.topleft = (x,y)
        self.clicked = False
    def desenhar(self):
        action = False
        #pegando a posição do mouse
        pos = pygame.mouse.get_pos()
            
        #checando se o mouse esta na area do botão e colocando respostas aos clique, e criando a variavel self.clicked para garantir o funcionamento do cliques
        if self.caixa.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
       
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #desenhar um botão na tela
        janela.blit(self.image,(self.caixa.x,self.caixa.y))


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