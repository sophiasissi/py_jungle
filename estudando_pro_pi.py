#-------------------------------
def new_game():
    guesses = []
    coerrect_guesses = 0
    question_num = 1
    
    for key in questoes:
        print("-------------------------------")
        print(key)
        for i in opicoes[question_num -1]:
            print(i)
        guess = input("coloque A B C ou D ")
        guess = guess.upper()
        guesses.append(guess) 
        coerrect_guesses =+ check_resposta(questoes.get(key), guess)
        question_num =+ 1
            
    
#-------------------------------
def check_resposta(answer, guess):
    if answer == guess:
        print("CERTO")
        return 1
    else:
        print("ERRADO kk ruim")
        return 0
    
#-------------------------------
def score(correct_guesses, guesses):
    print("-------------------------------")
    print("Resultado")
    print("-------------------------------")
    
    print("Respostas :", end="")
    for i in questoes:
        print(questoes.get(i), end=" ")
    print()
            
    print("Escolhas :", end=" ")
    for i in guesses:
        print(i, end="")
    print() 
    
    score = int(correct_guesses/len(questoes))*1000
    print("Sua pontuação é " + str(score)+"%")
#-------------------------------
def play_again():
    response = input("Você deseja jogar novamente? (Sim ou Não): ")
    response = response.upper()
    
    if response == "SIM":
        return True
    else:
        return False
#-------------------------------

questoes = {
"Quem criou o python?": "A",
"Em que ano o python foi criado o python? ": "B",
"Python é o nome de qual filme de comédia?": "C",
"Qual desse comandos servem para fazer um loop em python ": "A"
}

opicoes = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark ZuckerBurg"],
          ["A. 1989", "B. 1991", "C. 2000", "D.2016"],
          ["A.ELON MUSK FUDENDO O TWITTER +18", "B. O Grinch", "C. Monty Python", "D. Bill Gates e Elon Musk a 300km/h quem é mais corno?"],
          ["A. for", "B. input", "C. upper", "D. print"]]


new_game()

while play_again():
    new_game()
print("Fim do jogo")









