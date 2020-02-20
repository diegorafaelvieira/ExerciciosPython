#DESAFIO068 Limite:Aula15
#Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador perder, mostrando
#o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vit = 0

print('-='*5,'JOGO PAR OU ÍMPAR','=-'*5)
while True:
    j = int(input('Diga um valor: '))
    cpu = randint(0,10)
    tot = cpu + j
    t = ' '
    while t not in 'PI':
        t = str(input('PAR ou ÍMPAR? P/I: ')).strip().upper()[0]
    print(f'Você jogou {j} e escolheu {t}.')
    print(f'O Computador jogou {cpu}.')
    if t == 'P':
        if tot % 2 == 0:
            print('Venceu!Deu PAR')
            vit += 1
        else:
            print('PERDEU!')
            break
    elif t == 'I':
        if tot % 2 == 1:
            print('Venceu!Deu ÍMPAR')
            vit += 1
        else:
            print('PERDEU!')
            break
        print('Tente novamente...')
print(f'GAME OVER! Você venceu {vit} partida(s).')
