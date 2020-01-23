#DESAFIO049 Limite:Aula13
#Refaça o Desafio 009,mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

v = int(input('Digite o valor a ser tabulado: '))
print(f'Tabuada do {v}')
for c in range(1,11):
    print(f'{v} x {c} = {v*c}')
