#DESAFIO067 Limite:Aula15
#Faça um programa que mostre a tabuada de vários números, um de cada valor digitado pelo usuário. O programa
#será interrompido quando o número solicitado for negativo.


print('*='*5,'TABUADA','=*'*5)
while True:
    n = int(input('Informe o valor que deseja ver a tabuada ou qualquer valor negativo para sair: '))
    if n < 0:
        break
    print(f'TABUADA DO {n}')
    for c in range(1,11):
        tab = n * c
        print(f'{n} x {c} = {tab}')
print('FIM')