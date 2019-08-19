# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a)) # TIPO
print('Só tem espaços? ', a.isspace()) #SÓ TEM ESPAÇOS
print('É um número? ', a.isnumeric()) #É UM NÚMERO
print('É alfabético? ', a.isalpha()) #É ALFABÉTICO
print('É alfanumérico? ', a.isalnum()) #É ALFANUMÉRICO
print('Está em maiúsculas? ', a.isupper()) #É MAIÚSCULA
print('Está em minúscula? ', a.islower()) #É MINÚSCULA
print('Está capitalizada? ', a.istitle()) #É CAPITALIZADA