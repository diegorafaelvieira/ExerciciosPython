#DESAFIO071 Limite:Aula15
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
#ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possuí cédulas de R$50, R$20, R$10 e R$1.


n50 = n20 = n10 = n1 = 0

print('***'*5,'CAIXA ELETRÔNICO','***'*5)

v = int(input('Valor sacado R$ '))
tot = v
ced = 50
totCed = 0
while True:
    if tot >= ced:
        tot -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédula(s) de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if tot == 0:
            break
print('Saindo...')
