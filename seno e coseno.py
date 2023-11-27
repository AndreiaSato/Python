#SENO, COSENO E TANGENTE
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente desse ângulo
'''import math
a = float(input('Digite o ângulo que você deseja'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o ângulo {} tem o seno {:.2f} \n o ângulo {} tem o coseno {:.2f} \n o ângulo {} tem a tangente {:.2f}'.format(a,s,a,c,a,t))'''

#ou

from math import radians, sin,cos,tan
a=float(input('digite um ângulo'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('o ângulo {:.2f} tem seno{:.2f}, coseno{:.2f} e tangente {:.2f}'.format(a,s,c,t))

