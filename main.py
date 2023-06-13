import pygame
import time
import py_jungle_db_revisado
import login_pyjungle

# import Fases

#classe dos botões
class Button1():
    def __init__(self, x, y, largura, altura,pos):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.clicked = False
        self.pos = pos
    def verificar_clique(self):
        action = False
        pos_x,pos_y = pos
        if self.x - (self.largura/2) <= pos_x <= self.x + (self.largura/2) and self.y - (self.altura/2) <= pos_y <= self.y + (self.altura/2): 
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                #time.sleep(0.2)
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
        return action

class Fases():
    def __initt__(self):
        pass
    def ver_fase(self,level,pos):
        botao1 = False
        botao2 = False
        botao3 = False
        botao4 = False
        if 7 <= level <= 20 or level == 24 or 29 <= level <= 30 or 34 <= level <= 36:
            if level ==10 or level == 11 or level == 15 or 16 <= level <= 18:
                bt1 = Button1(351,499,703,999,pos)
                botao1 = bt1.verificar_clique()
                return botao1
            else:
                bt1 = Button1(234,551,135,168,pos)
                bt2 = Button1(471,548,140,84,pos)
                bt3 = Button1(236,766,131,169,pos)
                bt4 = Button1(473,766,135,171,pos)   
                botao1 = bt1.verificar_clique()
                botao2 = bt2.verificar_clique()
                botao3 = bt3.verificar_clique()
                botao4 = bt4.verificar_clique()
                print(botao1,botao2,botao3,botao4)
                return botao1,botao2,botao3,botao4
        elif level == 21 or level == 25 or level == 31:
            bt1 = Button1(220,547,136,166,pos)
            bt2 = Button1(476,544,132,168,pos)
            bt3 = Button1(359,764,138,172,pos)
            botao1 = bt1.verificar_clique()
            botao2 = bt2.verificar_clique()
            botao3 = bt3.verificar_clique()
            print(botao1,botao2,botao3)
            return botao1,botao2,botao3
        elif level == 26:
            bt1 = Button1(220,547,136,166,pos)
            bt2 = Button1(476,544,132,168,pos)
            botao1 = bt1.verificar_clique()
            botao2 = bt2.verificar_clique()
            return botao1,botao2  
        elif 22 <= level <= 23 or 27 <= level <= 28 or 32 <= level <= 33:
            bt1 = Button1(351,499,703,999,pos)
            botao1 = bt1.verificar_clique()
            return botao1

    
create_perguntas_table = """
CREATE TABLE IF NOT EXISTS Perguntas ( 
  idPerguntas INT NOT NULL AUTO_INCREMENT, 
  Perguntas_texto VARCHAR(300) NULL DEFAULT NULL, 
  PRIMARY KEY (idPerguntas) 
  ); 
 """
create_respostas_table = """
CREATE TABLE IF NOT EXISTS Respostas ( 
  idRespostas INT NOT NULL AUTO_INCREMENT, 
  idPerguntas INT NULL DEFAULT NULL, 
  Respostas_texto VARCHAR(200) NOT NULL, 
  Está_correto TINYINT NOT NULL, 
  PRIMARY KEY (idRespostas),
  CONSTRAINT Perguntas_resp FOREIGN KEY(idPerguntas) REFERENCES Perguntas(idPerguntas)
  ); 
"""
create_usuarios_table = """
CREATE TABLE IF NOT EXISTS Usuários ( 
  idUsuários INT NOT NULL AUTO_INCREMENT, 
  Username VARCHAR(30) NOT NULL, 
  Email VARCHAR(50) NULL DEFAULT NULL, 
  Login TINYINT NULL DEFAULT NULL, 
  Senha VARCHAR(45) NULL DEFAULT NULL, 
  É_Aluno TINYINT NULL DEFAULT NULL, 
  PRIMARY KEY (idUsuários) 
  ); 
"""
create_ranking_table = """
CREATE TABLE IF NOT EXISTS Ranking ( 
  idRanking INT NOT NULL AUTO_INCREMENT, 
  idUsuários INT NOT NULL, 
  Total_Acertos INT NULL DEFAULT NULL, 
  PRIMARY KEY (idRanking),
  FOREIGN KEY(idUsuários) REFERENCES Usuários(idUsuários)
  ); 
"""
create_perguntas_prof_table = """
CREATE TABLE IF NOT EXISTS Perguntas_Prof ( 
  idPerguntas_Prof INT NOT NULL AUTO_INCREMENT, 
  Perguntas_Prof_Texto VARCHAR(500) NULL DEFAULT NULL, 
  PRIMARY KEY (idPerguntas_Prof) 
  ); 
"""
create_respostas_prof_table = """
CREATE TABLE IF NOT EXISTS Respostas_Prof ( 
  idRespostas_Prof INT NOT NULL AUTO_INCREMENT, 
  idPerguntas_Prof INT NULL DEFAULT NULL, 
  Respostas_Prof_Texto VARCHAR(400) NULL DEFAULT NULL, 
  Está_correto TINYINT NOT NULL, 
  PRIMARY KEY (idRespostas_Prof),
  CONSTRAINT Perguntas_Respostas_Prof FOREIGN KEY(idPerguntas_Prof) REFERENCES Perguntas_Prof(idPerguntas_Prof)
  ); 
"""



pop_perguntas = """
INSERT INTO Perguntas (Perguntas_texto) VALUES  
  ('O que é programar? '), 
  ('Um algoritmo é uma sequência ______ e ______ de ações executáveis (instruções) que visam obter uma solução para um problema. Complete as lacunas com as palavras a seguir:'),
  ('Um programa é um conjunto de instruções escritas em uma _________ __ _________ que um computador executa para realizar uma determinada tarefa, ou seja, resolver um problema. Complete as lacunas com as palavras a seguir:'), 
  ('Quais são os componentes para criar uma variável e executá-la, por exemplo: valorA = 15.'), 
  ('Dentre os tipos abaixo quais deles são primitivos?'), 
  ('Quais dos nomes abaixo é correto para utilizar em nome de variável?'), 
  ('Qual alternativa abaixo tem a relação correta entre operadores e operação?'), 
  ('Qual é a sequência correta para Algoritmos Sequenciais?'), 
  ('Qual é o tipo de formatação de string abaixo?'), 
  ('Qual é a relação correta entre os operadores relacionais a seguir?'), 
  ('Qual é a definição correta do operador lógico not?'), 
  ('Complete a frase: Caso a condição definida no comando if seja falsa, o fluxo da execução do programa será redirecionado para o bloco de instruções alternativas declaradas na cláusula _____.'), 
  ('De acordo com o comando for, qual é a alternativa que possui a definição correta de item ou de conujunto_de_itens:'), 
  ('Qual é a saída desse código?'), 
  ('De acordo com a frase abaixo, isso significa que ela é executada também:  A cláusula else é executada sempre que o laço se encerra.'), 
  ('Qual é a saída desse código?'), 
  ('Qual é a saída desse código?'), 
  ('Qual item da lista foi removido? De acordo com o código abaixo:'); 
"""
pop_respostas = """
  INSERT INTO Respostas(idPerguntas, Respostas_texto, Está_correto) VALUES  
  (1,'Entender o problema e criar uma solução',1), 
  (1,'Criar um código e testá-lo',0), 
  (1,'Escrever um código em uma linguagem complexa',0), 
  (1,'Fazer manutenções de um código',0), 
  (2,'Não padronizada/ Consistente',0), 
  (2,'Padrão/ Inconsistente',0), 
  (2,'Finita/ Lógica',1), 
  (2,'Infinita/ Lógica',0), 
  (3,'Linguagem de Programação',1), 
  (3,'Linguagem de Máquina',0), 
  (3,'Linguagem de Alto Nível',0), 
  (3,'Linguagem de Baixo Nível',0), 
  (4,'Informação, Nome da variável e Código de execução',0), 
  (4,'Conteúdo da variável, Referência à um endereço e Código de execução',0), 
  (4,'Informação, Referência à um endereço na memória e Comando de atribuição',1), 
  (4,'Chave, Nome da variável e Comando de atribuição',0), 
  (5,'Inteiros, Pontos Flutuantes e Strings',1), 
  (5,'Listas, Strings e Booleans',0), 
  (5,'Inteiros, Booleans e Tuplas',0), 
  (5,'Pontos Flutuantes, Listas e Sets',0), 
  (6,'juquinha23, area_triangulo, valor!',0), 
  (6,'23juquinha, area_triangulo, \"numero\"',0), 
  (6,'maria55, altura retangulo, aspas+',0), 
  (6,'sophia21, valor_a, peso',1), 
  (7,'*(Multiplicação), //(Divisão Inteira)',1), 
  (7,'-(Subtração), *(Divisão)',0), 
  (7,'%(Divisão), +(Soma)',0), 
  (7,'/(Divisão Inteira), %(Modulo)',0), 
  (8,'Processamento com (+, -, *, /, //, %), print(), input()',0), 
  (8,'input(), processamento com (+, -, *, /, //, %), print()',1), 
  (8,'print(), processamento com (+, -, *, /, //, %), input()',0), 
  (8,'input(), print(), Processamento com (+, -, *, /, //, %)',0), 
  (9,'Placeholders',1), 
  (9,'Método .format()',0), 
  (9,'f-strings',0), 
  (10,'== (Comparação de igualdade), >= (Menor ou igual)',0), 
  (10,'<= (Menor), != (Comparação de diferença)',0), 
  (10,'>= (Maior ou igual), == (Comparação de igualdade)',1), 
  (10,'< (Menor), != (Comparação de igualdade)',0), 
  (11,'Nega(inverte) um valor lógico, ou seja, not True resulta em False, e not False resulta em True.',1), 
  (11,'Retorna True caso todas as condições componentes sejam True.',0), 
  (11,'Retorna True caso pelo menos uma das condições componentes seja True.',0), 
  (12,'Elif',0), 
  (12,'Else',1), 
  (13,'conjunto_de_itens: Pode ser uma lista, uma string, uma tupla, um dicionário ou qualquer objeto que permita iterações;',1), 
  (13,'item: Corresponde ao primeiro elemento pertencente ao conjunto_de_itens;',0), 
  (13,'conjunto_de_itens: Não pode ser uma lista, uma string, uma tupla, um dicionário ou qualquer objeto que permita iterações;',0), 
  (13,'item: Corresponde ao último elemento pertencente ao conjunto_de_itens.',0), 
  (14,'A',1), 
  (14,'B',0), 
  (14,'C',0), 
  (14,'D',0), 
  (15,'Depois de executar os primeiros itens do for.',0), 
  (15,'Quando a condição se torna falsa no while.',1), 
  (15,'Quando um laço é interrompido por um break.',0), 
  (16,'9',0), 
  (16,'16',0), 
  (16,'36',0), 
  (16,'25',1), 
  (17,'[9, 16]',0), 
  (17,'[4, 9, 16]',0), 
  (17,'[9, 16, 25]',1), 
  (17,'[16, 25, 36]',0), 
  (18,'36',1), 
  (18,'25',0), 
  (18,'16',0), 
  (18,'9',0); 
"""
        
        

if __name__ == '__main__':

###
    senhadb = 'tatubola18'
    hostwork = 'localhost'
    usuariowork = 'root'
    connection = py_jungle_db_revisado.create_server_connection(hostwork, usuariowork, senhadb)
    py_jungle_db_revisado.create_database(connection,'CREATE DATABASE IF NOT EXISTS py_jungle')
    connection = py_jungle_db_revisado.create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")
    py_jungle_db_revisado.execute_query(connection, create_perguntas_table)
    py_jungle_db_revisado.execute_query(connection, create_respostas_table)
    py_jungle_db_revisado.execute_query(connection, create_usuarios_table)
    py_jungle_db_revisado.execute_query(connection, create_ranking_table)
    py_jungle_db_revisado.execute_query(connection, create_perguntas_prof_table)
    py_jungle_db_revisado.execute_query(connection, create_respostas_prof_table)
    py_jungle_db_revisado.execute_query(connection, pop_perguntas)
    py_jungle_db_revisado.execute_query(connection, pop_respostas)

    usuario_entrado = login_pyjungle.entry1.get()
    password_entrado = login_pyjungle.entry2.get()
    #print(usuario_entrado)
    #print(password_entrado)
    #py_jungle_db_revisado.inserir_usuario(username, email, login, senha, e_aluno,,hostwork, usuariowork, senhadb)
    py_jungle_db_revisado.inserir_usuario(usuario_entrado, 'x', 1, password_entrado, 1,hostwork, usuariowork, senhadb)
    
    
    ruser_id_ret = py_jungle_db_revisado.execute_query_user_id(connection, f'select idUsuários from py_jungle.usuários where Username = "{usuario_entrado}"')
    w_user_id = ruser_id_ret
    id_usuario_w =w_user_id[0][0]
    ###print('aqui')
    ###print(id_usuario_w)
    

#######
    pygame.init()
    timer = pygame.time.Clock()
    #medidas da janela                ------------------- OLhar o minuto final do video para entender como utilizar isto como uma class em outros arquivos(video dos botões)------------------------------
    janela_altura = 1000 
    janela_largura = 707
    tela = []
    fonte = pygame.font.Font('imagem/myFont.ttf', 65)
    fps = 60
    screen = pygame.display.set_mode((janela_largura,janela_altura))
    pygame.display.set_caption('teste na aba')
    level = 7
    tela = (pygame.image.load(f'imagem/{level}.png'))    #usar de base para verificar os diretórios
    pontuacao = 0
    acerto = 1
    erro = 0
    run = True
    while run:
        timer.tick(fps)
        screen.fill('black')
        screen.blit(tela,(0,0))
        pos = pygame.mouse.get_pos()
        fs = Fases()
        if 7 <= level <= 20 or level == 24 or 29 <= level <= 30 or 34 <= level <= 36:
            if level ==10 or level == 11 or 15 <= level <= 18:
                botao1 = fs.ver_fase(level,pos)
            else:
                botao1,botao2,botao3,botao4 = fs.ver_fase(level,pos)
        elif level == 21 or level == 25 or level == 31:
            botao1,botao2,botao3 = fs.ver_fase(level,pos)
        elif level == 26:
            botao1,botao2 = fs.ver_fase(level,pos)
        elif 22 <= level <= 23 or 27 <= level <= 28 or 32 <= level <= 33:
            botao1 = fs.ver_fase(level,pos) 
        # print(pos)
        if level == 7:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level += 1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level += 1
            elif botao3 == True:
                pontuacao = pontuacao + acerto
                level += 1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level += 1
            print(level)

        elif level == 8:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + acerto
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)
        elif level == 9:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)
        elif level == 10:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 11:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 12:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level +=1         
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + acerto
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        elif level == 13:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1    
            print(level)  
        elif level == 14:
            if botao1 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + acerto
                level +=1    
            print(level)  
        elif level == 15:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 16:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 17:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 18:
            if botao1 == True:
               level +=1 
            print(level)  
        if level == 19:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level += 1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level += 1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level += 1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level += 1
            print(level)  
        elif level == 20:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + acerto
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        elif level == 21:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        elif level == 22:
            if botao1 == True:
               level +=1   
            print(level)  
        elif level == 23:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 24:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level +=1         
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + acerto
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        elif level == 25:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1    
            print(level)  
        elif level == 26:
            if botao1 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao2 == True:
                pontuacao = pontuacao + acerto
                level +=1
            print(level)  

        elif level == 27:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 28:
            if botao1 == True:
               level +=1 
            print(level)  
        elif level == 29:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        elif level == 30:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        if level == 31:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level += 1 
            elif botao2 == True:
                pontuacao = pontuacao + acerto
                level += 1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level += 1
            print(level)      
        elif level == 32:
            if botao1 == True:
               level +=1 
            print(level)     
        elif level == 33:
            if botao1 == True:
               level +=1 
            print(level)      
        elif level == 34:
            if botao1 == True:
               pontuacao = pontuacao + erro
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + acerto
                level +=1    
            print(level)  
        elif level == 35:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1 
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + acerto
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1    
            print(level)  
        elif level == 36:
            if botao1 == True:
               pontuacao = pontuacao + acerto
               level +=1         
            elif botao2 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao3 == True:
                pontuacao = pontuacao + erro
                level +=1
            elif botao4 == True:
                pontuacao = pontuacao + erro
                level +=1
            print(level)  
        
            
###
        ###elif level != 37:
        tela = (pygame.image.load(f'imagem/{level}.png'))
        screen.blit(tela,(0,0))
        if level == 37:
            pontu = fonte.render(str(pontuacao),True,(255))
            screen.blit(pontu,(351,520))
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                total_acertos = pontuacao
                #id_usuario = 1
                py_jungle_db_revisado.inserir_ranking(id_usuario_w, total_acertos,hostwork, usuariowork, senhadb)
 

        pygame.display.update()
    pygame.quit()

