#DESAFIO058 Limite:Aula14
#Melhore o jogo do DESAFIO028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
#jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep
palpite = ''
cont = 1
cpu = random.randint(0,10) #Faz o sorteio
palpite = int(input('Informe um número de 0 até 10: '))
print('Processando...')
sleep(2) #Aguarda 2 segundos
while palpite != cpu:
    print('Errou!')
    palpite = int(input('Informe um número de 0 até 10: '))
    cont += 1
    print('Processando...')
    sleep(2) #Aguarda 2 segundos
print(f'Foram necessários {cont} palpites até acertar o número escolhido pelo CPU.')
