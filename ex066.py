#DESAFIO066 Limite:Aula15
#Crie um programa que leia vários números inteiros pelo teclado.O programa só vai parar quando o usuário
#digitar o valor 999,que é a condição de parada.No final, mostre quantos números foram digitados e qual foi
#a soma entre eles(desconsiderando o flag).

c = s = 0
print('-='*20)
while True:
    n = int(input('Digite um número inteiro ou 999 para SAIR: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram informados {c} valores e a soma entre eles é igual a {s}.')
