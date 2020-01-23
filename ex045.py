#//DESAFIO045 Limite:Aula12
#Crie um programa que faça o computador jogar Jokenpô com você.
#->Pedra,papel e tesoura
#Sorteio para CPU

from random import randint

op = ('pedra','papel','tesoura')
print('''Escolha:
 0 - pedra
 1 - papel 
 2 - tesoura''')
eu = int(input('Opção: '))
print(f'Eu escolhi {op[eu]}')
cpu = (randint(0, 2))
print(f'O CPU escolheu {op[cpu]}')

if cpu == 0: #PEDRA
    if eu == 0:
        print('Empate!')
    elif eu == 1:
        print('Jogador venceu!')
    elif eu == 2:
        print('Cpu venceu')
elif cpu == 1: #PAPEL
    if eu == 0:
        print('Cpu venceu!')
    elif eu == 1:
        print('Empate!')
    elif eu == 2:
        print('Jogador venceu!')
elif cpu == 2: #TESOURA
    if eu == 0:
        print('Jogador venceu!')
    elif eu == 1:
        print('Cpu venceu!')
    elif eu == 2:
        print('Empate!')

