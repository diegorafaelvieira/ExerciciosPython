#DESAFIO039 Limite:Aula12
#Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do temnpo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today()
anoNasc = int(input('Digite o ano que nasceu: '))
idade = anoAtual.year - anoNasc

if idade < 18:
    tempo = 18 - idade
    print('Ainda vai se alistar ao serviço militar.')
    print(f'Falta {tempo} ano(s) para se alistar.')
elif idade == 18:
    print('É hora de se alistar.')
else:
    tempo = idade - 18
    print('Já passou o tempo de alistamento')
    print(f'Se passou {tempo} ano(s) para o alistamento.')