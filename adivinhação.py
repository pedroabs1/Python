import random

print(" ********************************")
print(" Bem vindo ao app de lotéria!")
print(" ********************************")
tentativa = 0
total_de_tentativas = 0
rodada = 1

numero_secreto = random.randrange(1, 101)

nivel = print("Escolha uma dificuldade (1) para facil (2) para medio e (3) para dificil)")

if(nivel == 3):
    total_de_tentativas = 10    
elif(nivel == 2):
    total_de_tentativas = 10    
else:
    total_de_tentativas == 1


for rodada in range(1, tentativa + 1):
    print(" Tentativa número ", tentativa, "de 3")
    print(" Tentativa número {} de 3" .format(tentativa))

    chute_str = input("Digite um número! ")

    print("Você digitou ", chute_str)
    chute = int(chute_str)


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("você acertou!")
        total_de_tentativas = 0
    else:
        print("Voce errou, tente novamente!")
        if(menor):
            print("Tente um número maior!")
        elif (maior):
            print("Tente um número menor!")
    tentativa = tentativa + 1


print("Fim do jogo!")
