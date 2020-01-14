#DESAFIO036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
#ele vai pagar.Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o salário: R$'))
anos = int(input('Digite a quantidade de anos que deseja pagar: '))

meses = anos * 12
valOk = (sal/100) * 30
parcelaMes = casa/meses


if parcelaMes <= valOk:
    print(f'O valor da parcela mensal é de R${parcelaMes:.2f}')
else:
    print('Empréstimo negado!')
