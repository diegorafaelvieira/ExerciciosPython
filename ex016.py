# DESAFIO 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
# ex:
# Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6
from math import trunc
num = float(input('Digite o valor: '))
print(f'O valor digitado foi {num} e a sua porção Inteira é {trunc(num)}')