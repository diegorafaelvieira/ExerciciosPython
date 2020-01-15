#//DESAFIO045 Limite:Aula12
#Crie um programa que faça o computador jogar Jokenpô com você.
#->Pedra,papel e tesoura
#Sorteio para CPU

import random
op = ['pedra', 'papel', 'tesoura']
cpu = (random.choice(op))
eu = str(input('Escolha: pedra, papel ou tesoura: '))
print(f'Eu escolhi {eu}')
print(f'O CPU escolheu {cpu}')
if eu == "pedra" and cpu == "tesoura" or eu == "tesoura" and cpu == "papel" or eu == "papel" and cpu == "pedra":
    print("Ganhou")
elif eu == "pedra" and cpu == "pedra" or eu == "tesoura" and cpu == "tesoura" or eu == "papel" and cpu == "papel":
    print("Empate")
else:
    print("Perdeu")