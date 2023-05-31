class Conta:
    def __init__(self,login, senha, email):
       self.login = login
       self.senha = senha
       self.email = email
    
    def verificar_login(self,login,senha):    
        if login == self.login:
            if senha == self.senha:
                return print('login autorizado')
            else:
                return print('Senha incorreta')
        else:
            return print('Login incorreto')    
        
login = input("Coloque  o login")
senha = input("coloque a senha")
email = input("Coloque o email")
conta = Conta(login,senha,email)
conta.verificar_login('Vitor','1234')