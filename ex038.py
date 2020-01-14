#DESAFIO038 Limite:Aula12
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
val1 = float(input('Digite o 1° valor: '))
val2 = float(input('Digite o 2° valor: '))
if val1 > val2:
    print('O primeiro valor é maior')
elif val1 < val2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais.')