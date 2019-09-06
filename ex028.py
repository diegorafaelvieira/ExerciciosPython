#DESAFIO028
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O computador deverá escrevar na tela se o usuário venceu ou perdeu
import random #Importa o RANDOM
from time import  sleep #Importa o SLEEP
cpu = random.randint(0,5) #Aqui sorteia
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
jog = int(input('Que número eu pensei: '))
print('PROCESSANDO...')
sleep(2) #Aguarda 2 segundos
if cpu == jog:
    print(f'Parabéns o Computador escolheu {cpu}!')
else:
    print(f'O Computador escolheu o número {cpu}.Tente novamente!')
