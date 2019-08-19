# DESAFIO 012 Limite:Aula07
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
val = float(input('Qual o preço do produto? R$'))
desc = val - (val * 5 / 100)
print(f'O preço com 5% de desconto é R${desc:.2f}')