class Botao:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
    
    def verificar_clique(self, pos_x, pos_y):
        if self.x <= pos_x <= self.x + self.largura and self.y <= pos_y <= self.y + self.altura:
            return True
        else:
            return False

# Exemplo de uso da classe
imagem = "imagem.png"  # Insira o caminho da imagem aqui

botao = Botao(100, 200, 50, 30)  # Posição (x, y) e dimensões (largura, altura) do botão

# Suponha que as coordenadas do clique sejam (120, 220)
posicao_x = 120
posicao_y = 220

if botao.verificar_clique(posicao_x, posicao_y):
    print("O botão foi clicado!")
else:
    print("O botão não foi clicado!")
