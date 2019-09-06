#DESAFIO032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date #Importa Date
ano = int(input('Qual ano deseja analisar?Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year  #Aqui pega o Ano Atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
