#DESAFIO033
#Faça um programa que leia três números e mostre qual é o maior e qual o menor.
n1 = int(input('Número 1:'))
n2 = int(input('Número 2:'))
n3 = int(input('Número 3:'))
#Verifica MENOR
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verifica MAIOR
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'MENOR: {menor}')
print(f'MAIOR: {maior}')