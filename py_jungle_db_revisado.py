import mysql.connector
from mysql.connector import Error
import pandas as pd
import sqlite3

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful\n")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    dbcursor = connection.cursor()
    try:
        dbcursor.execute(query)
        print("Database created successfully\n")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful\n")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        # Executar a consulta
        cursor.execute(query)
        ####if "Respostas" in query and "INSERT INTO" in query:
        ####    table_name = "Respostas"
        ####    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        ####    result = cursor.fetchone()
        ####    if result[0] > 0:
        ####        print(f"A tabela '{table_name}' já possui registros. A inserção não será executada.")
        ####        connection.rollback()
        ####        return
        connection.commit()
        print("Query successful\n")
    except Error as err:
        print(f"Error: '{err}'")
        
def execute_query_user_id(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            resultados = cursor.fetchall()
            return resultados
        except Error as err:
            print(f"Error: '{err}'")    
        
        

def inserir_pergunta_prof(texto_pergunta):
    # Conectar ao banco de dados
    connection = create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")

    try:
        # Inserir a pergunta na tabela
        query = f"INSERT INTO Perguntas_Prof (Perguntas_Prof_Texto) VALUES ('{texto_pergunta}')"
        execute_query(connection, query)
        print("Pergunta do professor inserida com sucesso!")
    except Error as err:
        print(f"Erro ao inserir a pergunta do professor: {err}")
    finally:
        # Fechar a conexão com o banco de dados
        if connection:
            connection.close()

def inserir_resposta_prof(id_pergunta_prof, texto_resposta, esta_correto):
    # Conectar ao banco de dados
    connection = create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")

    try:
        # Inserir as informações da resposta na tabela
        query = f"INSERT INTO Respostas_Prof (idPerguntas_Prof, Respostas_Prof_Texto, Está_correto) " \
                f"VALUES ({id_pergunta_prof}, '{texto_resposta}', {esta_correto})"
        execute_query(connection, query)
        print("Resposta do professor inserida com sucesso!")
    except Error as err:
        print(f"Erro ao inserir a resposta do professor: {err}")
    finally:
        # Fechar a conexão com o banco de dados
        if connection:
            connection.close()

def inserir_ranking(id_usuario, total_acertos,hostwork, usuariowork, senhadb):
    # Connect to the database
    connection = create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")

    try:
        # Insert the ranking information into the table
        query = f"INSERT INTO Ranking (idUsuários, Total_Acertos) VALUES ({id_usuario}, {total_acertos})"
        execute_query(connection, query)
        print("Ranking information inserted successfully!")
    except Error as err:
        print(f"Error inserting ranking information: {err}")
    finally:
        # Close the database connection
        if connection:
            connection.close()

def inserir_usuario(username, email, login, senha, e_aluno,hostwork, usuariowork, senhadb):
    # Conectar ao banco de dados
    connection = create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")

    try:
        # Inserir o usuário na tabela
        query = f"INSERT INTO Usuários (Username, Email, Login, Senha, É_Aluno) " \
                f"VALUES ('{username}', '{email}', {login}, '{senha}', {e_aluno})"
        execute_query(connection, query)
        print("Usuário inserido com sucesso!")
    except Error as err:
        print(f"Erro ao inserir o usuário: {err}")
    finally:
        # Fechar a conexão com o banco de dados
        if connection:
            connection.close()


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

    ### lógica principal
    ###
    senhadb = 'tatubola18'
    hostwork = 'localhost'
    usuariowork = 'root'
    connection = create_server_connection(hostwork, usuariowork, senhadb)
    create_database(connection,'CREATE DATABASE IF NOT EXISTS py_jungle')
    connection = create_db_connection(hostwork, usuariowork, senhadb, "py_jungle")
    execute_query(connection, create_perguntas_table)
    execute_query(connection, create_respostas_table)
    execute_query(connection, create_usuarios_table)
    execute_query(connection, create_ranking_table)
    execute_query(connection, create_perguntas_prof_table)
    execute_query(connection, create_respostas_prof_table)
    execute_query(connection, pop_perguntas)
    execute_query(connection, pop_respostas)
    
    
    ruser_id = execute_query_user_id(connection, "select idUsuários from py_jungle.usuários where Username = 'teste'")
    print(ruser_id[0][0])
    
    
# Exemplo de uso
    ##username = input("Digite o nome de usuário: ")
    ##email = input("Digite o email: ")
    ##login = int(input("Digite o valor para o campo Login (1 para True, 0 para False): "))
    ##senha = input("Digite a senha: ")
    ##e_aluno = int(input("Digite o valor para o campo É_Aluno (1 para True, 0 para False): "))
    ##
    ##inserir_usuario(username, email, login, senha, e_aluno)    
    
    
    #Exemplo de uso:
    id_usuario = int(input("Digite o valor para o campo id_usuário: "))
    total_acertos = int(input("Digite o valor do total de acertos: "))
    
    inserir_ranking(id_usuario, total_acertos)
    
    
    #Exemplo de uso:
    texto = input("Digite o texto da pergunta do professor: ")
    inserir_pergunta_prof(texto)
    
    
    id_pergunta_prof = int(input("Digite o id da pergunta do professor: "))
    texto_resposta = input("Digite a resposta da pergunta do professor: ")
    esta_correto = int(input("Digite o valor para o campo está correto (1 é True, 0 é False): "))
    
    inserir_resposta_prof(id_pergunta_prof, texto_resposta, esta_correto)
    
    
    
    
    
    
    

