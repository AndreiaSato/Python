# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA: [1]SOMA, [2] MULTIPLICAR, [3] MAIOR, [4] NOVOS NUMEROS, [5] SAIR DO PROGRMA.
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.



num = int(input('Digite primeiro valor: '))
num1 = int(input('Digite segundo valor: '))
opção = 0
while opção != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = num + num1
        print('seu resultado é: {}'.format(soma))
    elif opção == 2:
        multiplicar = num * num1
        print('seu resultado é: {}'.format(multiplicar))
    elif opção == 3:
        if num > num1:
            maior = num
        else:
            maior = num1
        print( 'entre o numero {} e o {}, o {} é o maior'.format(num, num1, maior))
    elif opção == 4:
        print('digite um novo numero')
        num = int(input('Primeiro valor:'))
        num1 = int(input('segundo valor:'))
    elif opção == 5:
        print('SAIR DO PROGRAMA!')
    print('Fim do Programa! Volte Sempre!!')



