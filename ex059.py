#DESAFIO059 Limite:Aula14
#Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 1 digitar valores/2 escolher a opção / até o loop digitar 5

v1 = v2 = op = 0

while op != 5:
    v1 = float(input('Digite o 1° valor: '))
    v2 = float(input('Digite o 2° valor: '))
    print('''
        SELECIONE A OPÇÃO DESEJADA:
        [1]-Somar
        [2]-Multiplicar
        [3]-Maior
        [4]-Novos Números
        [5]-Sair do programa
    ''')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        s = v1 + v2
        print(f'A soma entre {v1} + {v2} é igual a {s}')
    if op == 2:
        m = v1 * v2
        print(f'A multiplicação entre {v1} x {v2} é igual a {m}')
    if op == 3:
        if v1 > v2:
            print(f'{v1} é o maior valor')
        elif v1 < v2:
            print(f'{v2} é maior')
        else:
            print('Valores iguais')
    if op == 4:
        v1 = float(input('Digite o 1° valor: '))
        v2 = float(input('Digite o 2° valor: '))
        print('''
                SELECIONE A OPÇÃO DESEJADA:
                [1]-Somar
                [2]-Multiplicar
                [3]-Maior
                [4]-Novos Números
                [5]-Sair do programa
            ''')
        op = int(input('Digite a opção desejada: '))
    if op == 5:
        print('Saindo...')