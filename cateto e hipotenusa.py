#CATETO E HIPOTENUSA
#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo.
# Calcule e mostre o comprimento da hipotenusa
'''co = float(input('Digite o valor do cateto oposto'))
ca = float(input('digite o valor do cateto adjacente'))
h = (co**2 +ca**2)**(1/2)
print('Em um cateto oposto de {} e de um cateto adjacente de {} temos a hipotenusa {:.2f}'.format (co, ca,h ))'''

#ou

import math
co = float (input('digite o cateto oposto'))
ca = float (input('digite o cateto adjacente'))
h = math.hypot(co,ca)
print('em um cateto de {} e {}, a hipotenusa é {:.2f}'.format(co,ca,h))

#ou

from math import hypot
co = float(input('digite o cateto oposto'))
ca = float(input('digite o cateto adjacente'))
h = hypot(co,ca)
print(' em um cateto de {} e {} a hipotenusa mede {}'.format (co,ca,h))