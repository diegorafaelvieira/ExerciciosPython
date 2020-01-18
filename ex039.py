#DESAFIO039 Limite:Aula12
#Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do temnpo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o ano que nasceu: '))
idade = anoAtual - anoNasc
print(f'Quem nasceu em {anoNasc} tem {idade} anos')
if idade < 18:
    tempo = 18 - idade
    print(f'Falta {tempo} ano(s) para se alistar.')
    ano = anoAtual + tempo
    print(f'O ano do alistamento será {ano}')
elif idade == 18:
    print('Deve se alistar imediatamente.')
else:
    tempo = idade - 18
    print(f'Se passou {tempo} ano(s) para o alistamento.')
    ano = anoAtual - tempo
    print(f'Você deveria se alistar em {ano}')