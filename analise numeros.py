# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
'''num = int(input('DIGITE UM NÚMERO:'))
n = str(num)
print('Analisando o número{}'.format(num))
print('unidade: {}'.format(n[3]))
print('dezena:{}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar:{}'.format(n[0]))''' # este serve apenas para numeros com 4 ou mais digitos

num = int(input('DIGITE UM NÚMERO:'))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('ANALISANDO O NÚMERO {}'.format(num))
print('A UNIDADE: {}'.format(u))
print('A dezena: {}'.format(d))
print('A centena:{}'.format (c))
print('O milhar: {}'.format(m))
