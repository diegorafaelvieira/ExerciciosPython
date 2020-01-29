#DESAFIO060 Limite:Aula14
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex:
#5! = 5x4x3x2x1 = 120
#Fazer com WHILE E FOR

#WHILE
v = int(input('Digite o valor a ser fatorado: '))
fat = v
c = fat
while c != 1:
    c -= 1
    fat *= c
print(f'O fatoriral de {v} é {fat}.')


#FOR
v = int(input('Digite o valro a ser fatorado: '))
fat = v
for c in range(v,1,-1):
    c -= 1
    fat *= c
print(f'O fatorial de {v} é igual a {fat}.')

