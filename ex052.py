#DESAFIO052 Limite:Aula13
#Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo.
cont = 0
val = int(input('Digite o valor: '))
for c in range(1,val+1):
    if val % c == 0:
        cont+=1
if cont == 2:
    print(f'O número {val} é PRIMO')
else:
    print(f'O número {val} NÃO É PRIMO')
