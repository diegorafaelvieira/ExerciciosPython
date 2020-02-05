#DESAFIO058 Limite:Aula14
#Melhore o jogo do DESAFIO028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o
#jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
cont = 1
cpu = randint(0,10) #Faz o sorteio
palpite = int(input('Informe um número de 0 até 10: '))
print('Processando...')
sleep(2) #Aguarda 2 segundos
while palpite != cpu:
    print('Errou!')
    if cpu > palpite:
        print('Maior...Tente novamente.')
    elif cpu < palpite:
        print('Menor...Tente novamente.')
    palpite = int(input('Informe um número de 0 até 10: '))
    cont += 1
    print('Processando...')
    sleep(2) #Aguarda 2 segundos
print(f'Parabéns! Foram necessários {cont} palpites até acertar o número escolhido pelo CPU.')
