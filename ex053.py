#DESAFIO053 Limite:Aula13
#Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper() #MODO 1
palavras = frase.split(' ')
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')


frase = str(input('Digite uma frase: ')).strip().upper() #MODO 2
palavras = frase.split(' ')
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')

