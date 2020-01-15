#DESAFIO037 Limite:Aula12
#Escreva um programa que leia um número inteiro qualquer e peça para que o usuário escolher qual será a base de conversão
#-1 para binário
#-2 para octal
#-3 para hexadecimal

val = float(input('Digite o valor Decimal: '))
print('1 - para Binário')
print('2 - para Octal')
print('3 - para Hexadecimal')
op = int(input('Digite a opção desejada: '))
if op == 1:
    print(f'O valor {val} em Decimal é equivalente a {bin(int(val))} em Binário')
elif op == 2:
    print(f'O valor {val} em Decimal é equivalente a {oct(int(val))} em Octal')
elif op == 3:
    print(f'O valor {val} em decimal é equivalente a {hex(int(val))} em Hexadecimal')