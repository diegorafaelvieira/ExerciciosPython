# DESAFIO 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
area = a * l
lt = area / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {area}m²')
print(f'É necessário {lt} lt de tinta')