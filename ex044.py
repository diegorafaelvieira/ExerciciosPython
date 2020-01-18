#//DESAFIO044 Limite:Aula12
#Elabore um programa que calcule o valor a ser pago por um produto,considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão:5% de desconto
#- em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de juros

val = float(input('Digite o valor do produto R$'))
print('''Informe a condição de pagamento
1 - À vista em dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
cond = int(input('Condição: '))
if cond == 1:
    total = val - ((val/100) * 10)
    print(f'O valor do produto é de R${total:.2f} no dinheiro/cheque')
elif cond == 2:
    total = val - ((val/100) * 5)
    print(f'O valor do produto é de R${total:.2f} à vista no cartão')
elif cond == 3:
    total = val
    print(f'O valor do produto é de R${total:.2f} em até 2x no cartão')
elif cond == 4:
    parc = int(input('Quantidade de parcelas: '))
    total = val + ((val/100) * 20)
    val = total / parc
    print(f'O valor do produto é de R${total:.2f} em {parc} parcelas de R${val:.2f}')
else:
    print('Opção inválida!')
