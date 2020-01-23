#DESAFIO047 Limite:Aula13
#Crie um programa que mostre na tela todos os números pares que estão no intervalor entre 1 e 50.
for c in range(1,51):
    if(c % 2 == 0):
        print(c, end=' ')
print('FIM')

for c in range(2,51,2): # outra solução com menos iteração
    print(c, end=' ')
print('FIM')
