#//DESAFIO 027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o seu primeiro e o último nome separadamente
#Ex: Ana Maria de Souza
#primeiro=Ana
#último=Souza
nome = str(input('Digite o seu nome completo: '))
n = nome.split()
print('Primeiro: {}'.format(n[0]))
print('Último: {}'.format(n[len(n) - 1]))
