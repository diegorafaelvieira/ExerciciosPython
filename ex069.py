#DESAFIO069 Limite:Aula15
#Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se
#o usuário quer ou não continuar. No final, mostre:
# a)quantas pessoas tem mais de 18 anos.
# b)quantos homens foram cadastrados.
# c)quantas mulheres tem menos de 20 anos.

maior = m = f20 = 0

while True:
    id = int(input('Informe a idade: '))
    if id > 18:
        maior += 1
    s = ' '
    while s not in 'FM':
        s = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        m += 1
    if s == 'F' and id < 20:
        f20 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op == 'N':
        print(f'No total foram cadastrados {maior} pessoa(s) com mais de 18 anos.')
        print(f'Foram cadastrado(s) {m} homens.')
        print(f'Foram cadastradas {f20} mulher(es) com menos de 20 anos')
        break
print('Saindo...')
