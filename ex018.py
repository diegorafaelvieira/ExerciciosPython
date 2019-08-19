# DESAFIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin,cos,tan,radians
an = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f'O ângulo de {an} tem SENO de {seno:.2f}')
print(f'O ângulo de {an} tem COSSENO de {cosseno:.2f}')
print(f'O ângulo de {an} tem TANGENTE de {tangente:.2f}')