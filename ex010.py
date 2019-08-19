# DESAFIO 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3,27  E$1.00 = R$4.21
r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r / 3.27
e = r / 4.21
print(f'Com R${r:.2f} você pode comprar US${d:.2f} ou E${e:.2f}')