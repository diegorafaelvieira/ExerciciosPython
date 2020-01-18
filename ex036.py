#DESAFIO036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
#ele vai pagar.Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o salário: R$'))
anos = int(input('Digite os anos do financiamento: '))

meses = anos * 12
valOk = (sal/100) * 30
parcela = casa/meses

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${parcela:.2f}')

if parcela <= valOk:
    print(f'Empréstimo autorizado!')
else:
    print('Empréstimo negado!')
