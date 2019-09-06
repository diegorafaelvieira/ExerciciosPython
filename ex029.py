#DESAFIO029 Limite:Aula10
#Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.
vel = float(input('Informe a velocidade atual do carro:'))
if vel > 80:
    multa = (vel - 80) * 7.00
    print(f'MULTA!Acima de 80km/h!Multa de R${multa:.2f}')
print('Dirija com segurança!')
