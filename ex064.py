#DESAFIO064 Limite:Aula14
#Crie um programa que leia vários números inteiros pelo teclado.O programa só vai parar quando o usuário
#digitar o valor 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual foi a
#soma entre eles (desconsiderando o flag).

c = n = s = 0

while n != 999:
    n = int(input('Digite um valor inteiro qualquer ou 999 para sair: '))
    if n != 999:
        c += 1
        s += n
print(f'Foram digitados {c} números e a soma entre eles é de {s}.')
