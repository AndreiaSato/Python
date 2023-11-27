#TRABALHANDO COM MÓDULOS
'''import math
num = int(input('digite um numero'))
raiz =math.sqrt(num)
print('a raiza de {} é igual a {}'.format(num, math.ceil(raiz)))'''
#ou
'''from math import sqrt
num = int(input('digite um numero'))
raiz = sqrt (num)
print(' a raiz de {} é igual a {}'.format(num,raiz))'''
#QUEBRANDO UM NÚMERO
# crie um programa que leia um numero real qualquer e mostre na tela a sua porção inteira
# ex: digite um numero: 6.127 O numero 6.127 tem a porção inteira 6 (trunc - cortar a parte inteira de um numero
'''import math
num = float(input('Digite um número'))
print('o valor digitado foi {} e a sua porção inteira é {}'.format (num, math.trunc(num)))'''
#ou
'''from math import trunc
num = float(input('Digit um número'))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc (num)))'''
#ou
num = float(input('digite um valor'))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))


