#DESAFIO035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = float(input('Digite o valor do 1° lado:'))
l2 = float(input('Digite o valor do 2° lado:'))
l3 = float(input('Digite o valor do 3° lado:'))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('É um TRIÂNGULO')
else:
    print('Não É TRIÂNGULO')
