#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas
#-o nome com todas minúsculas
#-Quantas letras aotodo[sem considerar espaços]
#-Quantas letras tem o primeiro nome

nome = str(input("Digite o seu nome completo: ")).strip()
print(f'O seu nome é {nome}')
print(f'O seu nome em maiúsculo é {nome.upper()}')
print(f'O seu nome em minúsculo é {nome.lower()}')
print('O seu nome tem ao todo tem {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possuí {}'.format(nome.find(' ')))