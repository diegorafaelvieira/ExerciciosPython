#DESAFIO056 Limite:Aula13
#Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas.No final do programa,mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.


idade = 0
totIdade = 0
mediaIdade = 0
femIdMenor = 0
maiorIdadeH = 0
nomeVelhoH = ''
for c in range(1, 5):
    print(f'---> {c}ª Pessoa:')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    totIdade += idade
    sexo = str(input('Sexo: [M / F]: ').upper())
    if c == 1 and sexo == 'M':
        maiorIdadeH = idade
        nomeVelhoH = nome
    if sexo == 'M' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeVelhoH = nome
    if sexo == 'F' and idade < 20:
        femIdMenor += 1
mediaIdade = totIdade/4
print(f'A média da idade do grupo é de {mediaIdade:.2f} anos.')
print(f'O nome do homem mais velho que tem {idade} anos é{nomeVelhoH}.')
print(f'Ao todos temos {femIdMenor} mulher(es) com menos de 20 anos.')