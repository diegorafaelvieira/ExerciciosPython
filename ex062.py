#DESAFIO062 Limite:Aula14
#Melhore o DESAFIO061, perguntando para o usuário se ele quer mostrar mais alguns termos.O programa encerra
#quando ele disser que quer mostrar 0 termos.


a1 = int(input('Informe o 1° termo da PA: '))
r = int(input('Informe a razão: '))
c = 1
val = a1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{val} ->', end='')
        val += r
        c += 1
    print('PAUSE')
    print('''Deseja mostrar mais alguns termos?
    [n] - Digite a quantidade de termos desejados
    [0] - Para sair: ''')
    mais = int(input('Opção: '))
print('FIM')


