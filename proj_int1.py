# Importação da biblioteca que fornece números aleatórios
import random

# definição de uma função principal responsável pelo código
def adivinhacao():
    numero = random.randrange(1,100) # função que escolhe um número aleatório no intervalo definido
    # e armazena o valor na variável numero

    tentativas = 0 # criada uma variável para a contagem das tentativas do usuário

    print("Olá, bem vindo ao jogo de adivinhação! \n\nNesse jogo voce deve informar um numero de sua escolha "
          "com o objetivo de acertar o numero escolhido pela maquina!!! \nVoce terá 4 chances para tentar adivinhar "
          "o numero sorteado!!! \n   --- BOA SORTE ---\n") # texto de apresentação ao usuário

    while True:  # laço que contará as tentativas e verifica a entrada do usuário com o valor aleatório gerado

        entrada = int(input("Tente adivinhar o numero: ")) # Armazenamento do valor de entrada do usuário

        if entrada == numero:   # primeira verificação do valor digitado e a ação condicionada
            print("\nParabens, voce acertou!!!!\n")
            break # palavra reservada que tem a função de parar o funcionamento do sistema na condição de acerto do numero

        elif entrada < numero: # segunda verificação do valor digitado seguido da condição determinada
            print("O numero é maior que isso!!!\n")
            tentativas += 1 # incremento da quantidade de tentativas caso não acerte o numero

        elif entrada > numero:  # terceira verificação do valor e sua ação
            print("O numero é menor que esse!!!\n")
            tentativas += 1

        if tentativas >= 4:  # condicional que encerra o jogo caso a quantidade de tentativas seja ultrapassada
            print("Desculpe, seu limite de tentativas excedeu!!!")
            print("O numero sorteado foi: ",numero) # texto informando o valor gerado caso não tenha sucesso nas tentativas
            break

adivinhacao() # chamada da função principal responsavel pelo jogo