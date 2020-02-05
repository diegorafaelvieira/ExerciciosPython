#DESAFIO060 Limite:Aula14
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex:
#5! = 5x4x3x2x1 = 120
#Fazer com WHILE E FOR

#WHILE
v = int(input('Digite o valor a ser fatorado: '))
c = v
fat = 1
print(f'O fatorial de {v}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print('X ' if c > 1 else '= ', end='')
    fat *= c
    c -= 1
print(f'{fat}.')


#FOR
v = int(input('Digite o valor a ser fatorado: '))
f = 1
print(f'O fatorial de {v}! =', end=' ')
for c in range(v,0,-1):
    print(f'{c}', end=' ')
    print('X ' if c > 1 else '= ', end='')
    f *= c
print(f'{f}.')

