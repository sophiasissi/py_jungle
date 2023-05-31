import pygame
import botaofinal

class Fases():
    def __initt__(self,level,pos):
        self.level = level
        self.pos = pos
    def ver_fase(self):
        if 7 <= self.level >= 20 or self.level == 24 or 29<= self.level >= 30 or 34 <= self.level >= 36:
            botao1 = botaofinal.Button1(234,551,135,168,self.pos)
            botao2 = botaofinal.Button1(471,548,140,84,self.pos)
            botao3 = botaofinal.Button1(236,766,131,169,self.pos)
            botao4 = botaofinal.Button1(473,766,135,171,self.pos)
        return botao1,botao2,botao3,botao4
        
            
            
        
        
