#DESAFIO070 Limite:Aula15
#Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
# a)Qual o total gasto na compra.
# b)Quantos produtos custam mais de R$1000.
# c)Qual é o produto mais barato.

s = mil = menor = c = 0
nomeB = ''

print('=='*7,'PRODUTOS','=='*7)

while True:
    p = str(input('Produto: '))
    v = float(input('Preço: R$ '))
    s += v
    c += 1
    if v > 1000:
        mil += 1
    if c == 1:
        menor = v
        nomeB = p
    else:
        if v < menor:
            menor = v
            nomeB = p
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        print(f'Total gasto R${s:.2f}')
        print(f'{mil} produto(s) custa(m) mais que R$1000.')
        print(f'O produto mais barato foi {nomeB} e custa R${menor:.2f}.')
        break
print('Saindo...')