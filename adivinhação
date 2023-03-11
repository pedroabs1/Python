print(" ********************************")
print(" Bem vindo ao app de lotéria!")
print(" ********************************")

tentativas = 1
#numero_secreto = 42
#numero_aleatorio = random.random() * 100
#numero_secreto = round numero_aleatorio

numero_secreto = random.randrange(1, 101)

while(tentativas <= 3):

print(" Tentativa número ", tentativas, "de 3")
print(" Tentativa número {} de 3" .format(tentativas))

chute_str = input("Digite um número! ")

print("Você digitou ", chute_str)
chute = int(chute_str)

#if(chute == numero_secreto):
#    print("Parabéns você acertou!")
#else:
#    print("Voce errou, tente novamente!")
#    if(chute < numero_secreto):
#        print("Tente um número menor!")
#    else:
#        print("Tente um número maior!")
#print("Fim do jogo!")

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
     print("você acertou!")
     tentativas = 0
else:
    print("Voce errou, tente novamente!")
    if(menor):
        print("Tente um número maior!")
    elif (maior):
        print("Tente um número menor!")
tentativas = tentativas + 1
print("Fim do jogo!")
