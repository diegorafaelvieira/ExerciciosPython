#DESAFIO050 Limite:Aula13
#Desenvolvendo um programa que leia seis números inteiros e mostre a soma apenas daqueles
#que forem pares.Se o valor for ímpar, desconsidere-o.
s = 0
for c in range(1,7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        s += num
print(f'A soma dos valores pares informados é: {s}')