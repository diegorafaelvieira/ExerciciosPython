#DESAFIO054 Limite:Aula13
#Crie um programa que leia o ano de nascimento de sete pessoas.No final, mostre quantas pessoas
#ainda não atingiram a maioridade e quantas já são maiores. (21 anos)

from datetime import date

maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(f'Digite o {c}° ano de nascimento: '))
    atual = date.today().year
    idade = atual-nasc
    if idade >= 21:
        maior+=1
    else:
        menor+=1
print(f'{menor} pessoas não atingiram a maioridade.')
print(f'{maior} pessoas já atingiram a maioridade.')