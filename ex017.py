# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
op = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente:'))
hip = hypot(op, adj)
print(f'A hipotenusa do triângulo vai medir {hip:.2f}')