# DESAFIO 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o salário R$'))
ns = sal + (sal * 15 / 100)
print(f'Salário antigo era R${sal:.2f}')
print(f'Novo salário com aumento de 15% é R${ns:.2f}')