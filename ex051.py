#DESAFIO051 Limite:Aula13
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final mostre os 10 primeiros termos dessa progressão.

a1 = int(input('1° termo: '))
r = int(input('Razão: '))
a10 = a1 + (10-1) * r
for c in range(a1,a10+r,r):
    print(c,end=' -> ')
print('FIM')