# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
nu = int(input('DIGITE UM NÚMERO:'))
resultado = nu % 2
if resultado == 1:
    print ('Você digitou um número ímpar!')
else:
    print('o número é PAR')
