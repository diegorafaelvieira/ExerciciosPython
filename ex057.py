#DESAFIO057 Limite:Aula14
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper() #elimina espaços | converte para maíusculo
while sexo not in 'MF':
    print('Dados inválidos!')
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
print(f'Você informou o sexo {sexo} com sucesso!')
print('FIM')
