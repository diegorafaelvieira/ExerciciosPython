#//DESAFIO042 Limite:Aula12
#Refaça o DESAFIO035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero:todos os lados iguais
#- Isósceles:dois lados iguais
#- Escaleno:todos os lados diferentes
#->é triângulo ou não pode ser um triângulo

l1 = float(input('Informe o lado 1: '))
l2 = float(input('Informe o lado 2: '))
l3 = float(input('Informe o lado 3: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Triângulo ', end='') # AQUI COLOCA O TIPO DO TRIÂNGULO PRINT AO LADO
    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 and l2 != l3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é triângulo')