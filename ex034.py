#DESAFIO034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250.00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite o salário R$ '))
if sal > 1250:
    nsal = sal + (sal/100)*10
else:
    nsal = sal + (sal/100)*15
print(f'O salário de R$ {sal:.2f} passa para R${nsal:.2f}')
