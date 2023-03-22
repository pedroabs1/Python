print("****************************")
print("Bem vindo ao app de lotéria!")
print("****************************")

chute_str = input("Digite um número! ")
chute = int(chute_str)
numero_secreto = 42

if(chute == numero_secreto):
    print("Parabéns você acertou!")
else:
    print("Voce errou, tente novamente!")
    if(chute < numero_secreto):
        print("tente um número menor!")
    else:
        print("tente um número maior!")
print("fim do jogo!")
