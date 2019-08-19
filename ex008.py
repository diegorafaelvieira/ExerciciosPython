# DESAFIO 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
md = float(input('Distância em metros: '))
dm = md * 10
cm = md * 100
mm = md * 1000
dam = md / 10
hm = md / 100
km = md / 1000
print(f'{md} mt é igual a {km} km')
print(f'{md} mt é igual a {hm} hm')
print(f'{md} mt é igual a {dam} dam')
print(f'{md} mt é igual a {dm:.0f} dm')
print(f'{md} mt é igual a {cm:.0f} cm')
print(f'{md} mt é igual a {mm:.0f} mm')