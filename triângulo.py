# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
p = float(input('Digite o primeiro segmento:'))
s = float(input('Digite um segundo segmento:'))
t = float(input('Digite um terceiro segmento:'))
if p < s+t and s < p+t and t < p+s:
    print('PODEM se formar um triangulo')
else:
    print('NÃO PODEM formar um triangulo')
