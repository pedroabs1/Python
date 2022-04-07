# print('Migracao ',' borboletas ',' monarcas')
#nome = input('Qual o seu nome?')
#print(nome)

#n1=int(input('Digite um número ? '))
#n2=int(input('Digite outro número ? '))
#print(type(n2))
#soma=n1+n2
#print(soma)

#print('A soma do número',n1,'e o número',n2,'é:',soma)
#print('A soma do número {0} e o número {1} vale: {2}'.format(n1,n2,soma))

#t1=input('Digite algo: ')
#print(t1.isnumeric()) # numero
#print(t1.isalpha()) #alfabetico
#print(t1.isalnum()) #alfanumérico
#print(t1.isupper()) # maiúscula

#t1=int(input('Digite algo: '))
#print('voce digitou: {0} seu valor anterior é:{1},seu valor posterior é:{2}sua raiz quadrada é:{3},sua raiz cubica é:{4}'.format(t1,t1-1,t1+1,t1*(1/2),t1*(1/3))) 

#n1 = int(input( 'Digite a primeira nota do aluno: '))
#n2 = int(input( 'Digite a segunda nota do aluno: '))
#print('A média do aluno é:{}'.format((n1+n2)/2))

#metros = int(input('Digite um valor em metros para ter a sua conversão em cm mm e km: '))
#print(' O valor digitado foi: {}m, em cm vale: {}cm, em mm vale: {}mm e em km vale: {}km'.format(metros,metros*100,metros*1000,metros/1000))

#print('='*20,'Tabuada','='*20)
#tab = int(input('Digite um número qualquer e tenha sua tabuada completa: '))
#print('O número digitado foi: {},\n {}x1={}\n {}x2={}\n {}x3={}\n {}x4={}\n {}x5={}\n {}x6={}\n {}x7={}\n {}x8={}\n {}x9={}\n {}x10={}'.format(tab,tab,tab*1,tab,tab*2,tab,tab*3,tab,tab*4,tab,tab*5,tab,tab*6,tab,tab*7,tab,tab*8,tab,tab*9,tab,tab*10))

#print('$'*20,'Conversor de moedas','$'*20)
#t1=float(input('Digite a cotação atual: '))
#t2=float(input('Digite o valor para converter em dólares: '))
#print('O valor em reais {0}, co sem a cotação atual {1}, voce teria {2} dolares!'.format(t1,t2,t1/t2)) 

#a1 = int(input('Digite a altura da parede: '))
#l1 = int(input('Digite a largura da parede: '))
#print('Serão necessários {:.2f} litros de tinta para pintar {:.2f}m2'.format((a1*l1)/2,a1*l1))

#s1 = int(input('Qual o seu salário? '))
#print('Seu novo salário será: {}'.format(s1*1.05))


#dia = int(input('Quantos dias vc alugou o carro? '))
#km = int(input('Quantos km vc percorreu com o carro? '))
#pago = (km*0.15)+(dia*60)
#print(pago)
#print('O custo total do aluguel é:R${:.2f}'.format(pago))
#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print(' A raiz quadrada do número {} é: {:.2f}'.format(num,raiz))

#import random
#num = random.randint(1, 1000000000)
#print(num)

#import math
#num = float(input('digite um número: '))
#low = math.floor(num)
#high = math.ceil(num)
#print('vc digitou: {} arrendondado para baixo fica : {:.2f} e para cima: {:.2f}'.format(num ,low, high))

# import math
#num = float(input('digite um número: '))
#print('vc digitou: {} a parte inteira é: {}'.format(num ,math.trunc(num)))

#num = float(input('digite um número para converter para Kelvin e Fahrenheit: '))
#print('vc digitou: {}, que em Farenheit vale: {}°F e em Kelvin é: {}°K'.format(num,(1.8*num)+32,(num+273)))

# import math
# co = float(input('digite o cateto oposto: '))
# ca = float(input('digite o cateto adjacente: '))
# hyp = math.sqrt((co**2)+(ca**2))
# print('A hipotenusa vale: {}'.format(hyp))
# ou
# import math
# co = float(input('digite o cateto oposto: '))
# ca = float(input('digite o cateto adjacente: '))
# hyp = math.hypot(co, ca)
# print('A hipotenusa vale: {}'.format(hyp))

# import math
# num = float(input('digite um numero: '))
# sen = math.sin(num)
# cos = math.cos(num)
# tan = math.tan(num)
# print('O Seno vale: {}, o cosseno vale: {}, a tangente vale: {}'.format(sen, cos, tan))

# import random
# a1 = input('qual o nome do primeiro aluno: ')
# a2 = input('qual o nome do segundo aluno: ')
# a3 = input('qual o nome do terceiro aluno: ')
# a4 = input('qual o nome do quarto aluno: ')
# lista = [a1, a2, a3, a4]
# print('O o aluno escolhido é: {}'.format(random.choice(lista)))

# import pygame
# pygame.init()
# pygame.mixer.music.load('maguilafaleceu.mp3') #PLSTBANG.wav
# pygame.mixer.music.play()

# frase = 'Curso em Video Python'

# # C u r s o   e m   V i  d  e  o     P  y  t   h  o  n
# # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# print(frase[9])  # = V
# print(frase[9:13]) # = Video
# print(frase[9:13:2]) # = VdoPto
# print(frase[:5]) # = Curso
# print(frase[15:]) # = Python
# print(frase[9::3]) # = VePh
# print(frase[9::3]) # = VePh

# len[frase] # = 21

# frase.count('o') # = 3
# frase.count('o', 13, 1)  # = 1

# frase.find('deo') # = 11
# frase.find('Android') # = -1

# 'Curso' in frase # = true
# frase = frase.replace('Python','Android') # frase = 'Curso em Video Android'

# frase.upper() # Maiusculas
# frase.lower() # Minusculas

# frase.capitalize() # primeira letra em Maiusculas
# frase.title()  # primeira letra em todas palavras Maiusculas

# frase.strip() # remove espaços antes e depois
# frase.rstrip() # remove espaços na direita
# frase.lstrip() # remove espaços na esquerda

# frase.split() # divide string pelo espaços e transforma em lista
# # C u r s o   e m   V i  d  e  o     P  y  t   h  o  n
# #     0        1         2                   3        

# ' '.join(frase ) # une a frase acima 

# frase = 'Curso em Video Python'
# dividido = frase.split()
# print(dividido[1])  # = em
# print(dividido [2] [3])  # = e de vidEo


# print("""The Mersenne Twister is a pseudorandom number generator (PRNG). It is by far the most widely used general-purpose PRNG.[1] Its name derives from the fact that its period length is chosen to be a Mersenne prime.

# The Mersenne Twister was developed in 1997 by Makoto Matsumoto [ja] (松本 眞) and Takuji Nishimura (西村 拓士).[2] It was designed specifically to rectify most of the flaws found in older PRNGs.

# The most commonly used version of the Mersenne Twister algorithm is based on the Mersenne prime 219937−1. The standard implementation of that, MT19937, uses a 32-bit word length. There is another implementation (with five variants[3]) that uses a 64-bit word length, MT19937-64; it generates a different sequence.""")

# nome = input('Digite seu nome completo: ')
# nomeMaiusculo = nome.upper()
# nomeMinusculo = nome.lower()
# comprimentoNome = len(nome)
# espaços = nome.count(' ')
# dividir = nome.split()
# numLetrasPrimeiroNome = len(dividir [0])
# nomeSemEspaços = comprimentoNome - espaços
# print('Vc digitou: {}, em minusculas é: {}, em maiusculas: {}, e tem o comprimento total de: {}, caracteres, descontando os espaços, e o numero de letras do primeiro nome é: {}.'.format(nome, nomeMinusculo, nomeMaiusculo, nomeSemEspaços, numLetrasPrimeiroNome))

# Numero = input('Digite um numero entre 0 e 9999: ')
# unidade = Numero [3]
# dezena = Numero [2]
# centena = Numero [1]
# milhar = Numero [0]
# ou 
# unidade = Numero [3]
# dezena = Numero [2]
# centena = Numero [1]
# milhar = Numero [0]

# print("""Unidade: {}
# Dezena: {}
# Centena: {}
# Milhar: {}""".format(unidade, dezena, centena, milhar))

# cidade = input('Digite um nome de uma cidade: ')   
# print('A cidade tem Santo? {}'.format('santo' in cidade))

# nome = input('Digite seu nome completo: ')   
# print('Seu nome tem silva? {}'.format('silva' in nome))

# frase = str(input('Digite uma frase: ')).lower().strip()
# numA = frase.count('a')
# PosiçãoPrimeiroA = frase.find('a')+1 
# PosiçãoUltimoA = frase.rfind('a')+1
# print("""A letra A aparece {} vezes na frase.
# A primeira ocorrencia esta na posição {} 
# A ultima ocorrencia esta na posição {}""".format(numA,  PosiçãoPrimeiroA, PosiçãoUltimoA))

# nome = str(input('Digite seu nome: ')).lower().strip()
# nome = nome.split()
# print(""" Seu primeiro nome é: {} 
# Seu ultimo nome é: {}""".format(nome[0] , nome[len(nome)-1]))

# import random
# num = int(input('Adivinhe um numero de 1 a 5 escolhido pelo computador: '))
# numComputador = random.randint(1, 5)
# print(num , numComputador)
# if (num == numComputador):
#     print('voce acertou parabens! ')
# else:
#     print('voce errou tente novamente! ')


# velocidade = int(input('digite a velocidade do carro em km: '))
# print(velocidade)
# if (velocidade > 80):
#     print('Voce esta acima do limite de velocidade e sera multado em R${},00'.format((velocidade-80)*7))
# else:
#     print('Voce esta abaixo do limite de velocidade parabens')

# import math 
# num = int(input('digite numero para saber se ele é par ou impar: '))
# print(num)
# if (num%2) == 0:
#     print('Este numero é par')
# else:
#     print('Este numero é impar')

# distanciakm = int(input('digite a distancia da viagem em km: '))
# print(distanciakm)
# if (distanciakm <= 200):
#     print('Voce pagará R${}'.format(distanciakm*.5))
# else:
#     print('Voce pagará R${}'.format(distanciakm*.45))

# from datetime import date
# ano = int(input('digite um ano para saber se e bissexto ou zero para verificar o ano atual: '))
# # print(ano)
# if ano == 0:
#     ano = date.today().year
# if (ano%4) == 0 and (ano%100) == 0 and (ano%400) == 0:
#     print('o ano {} é bissexto!'. format(ano))
# else:
#     print('o ano {} não é bissexto!'. format(ano))

n1 = input('digite um numero: ')
n2 = input('digite um numero: ')
n3 = input('digite um numero: ')

# # lista = [a1, a2, a3, a4]
# print('O o aluno escolhido é: {}'.format(random.choice(lista)))
