#DESAFIO061 Limite:Aula14
#Refaça o DESAFIO051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.

a1 = int(input('Informe o 1° termo da PA: '))
r = int(input('Informe a razão: '))
c = 1
val = a1

print(a1,end='->')
while c < 10:
    val += r
    c += 1
    print(val, end='->')

