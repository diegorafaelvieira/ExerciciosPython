# //DESAFIO041 Limite:Aula12
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos:JUNIOR
# - Até 20 anos:SÊNIOR
# - Acima:MASTER

from datetime import date

anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade == 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
