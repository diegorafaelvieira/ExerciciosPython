#DESAFIO065 Limite:Aula14
#Crie um programa que leia vários números inteiros pelo teclado.No final, mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer
#continuar ou não continuar a digitar valores.

c = maior = menor = soma = media = 0
r = 'S'

while r != 'N':
    v = int(input('Digite um valor: '))
    r = str(input('Continuar? [S/N]: ')).strip().upper()[0]
    soma += v
    c += 1
    if c == 1:
        maior = c
        menor = c
    else:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
media = soma / c
print(f'Valores informados: {c}')
print(f'Média: {media:.2f}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')



