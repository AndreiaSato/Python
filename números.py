'''n1 = int(input('digite um número:'))
n2 = int(input('digite outro numero:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {},o produto é {}, e a divisão é {:.3f}'.format(s,m,d),end=' >>>')
print('a divisão inteira é {} e a potência é {:.2f}'. format (di,e))'''
#faça um programa que leia um numero inteiro e mostre na tela seu secessor e antecessor
'''n1=int(input('Digite um número'))
su=n1+1
an=n1-1
print('O sucessor do número {}, é {} e seu entecessor é {}'.format(n1,su,an))'''
# crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''n1=int(input('digite um número'))
do=n1*2
tr=n1*3
ra=n1**(1/2)
print("o dobro desse número é {}, o triplo {}, e sua raiz quadrada,{:.2f} ".format(do,tr,ra))'''
# desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
'''n1=int(input('qual a primeira nota?'))
n2=int(input('qual sua segunda nota?'))
s=n1+n2
m=s/2
print('sua média é',(m))'''
# escreva um programa que leia um valor em metros e exiba convertido em centímetros e milimitros
'''n1= float(input('quantos metros você tem?'))
cm= n1*100
m= n1*1000
print('você tem',(n1), 'metros', (cm),'cntimetro,e',(m), 'milimetros')'''
# faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
'''n=int(input('qual número quer saber a tabuada?'))
n1=n*2
n2=n*3
n3=n*4
n4=n*5
n5=n*6
n6=n*7
n7=n*8
n8=n*9
n9=n*10
print(('a tabuada do número,{} é {} {} {} {} {} {} {} {} {}').format(n,n1,n2,n3,n4,n5,n6,n7,n8,n9))'''
# outra forma da tabuada
'''n = int(input('digite um número:'))
print('{} * {:2} = {}'.format(n, 1,n*1))
print('{} * {:2} = {}'.format(n, 2, n*2))
print('{} * {:2} = {}'.format(n,3, n*3))
print('{} * {:2} = {}'.format(n, 4, n*4))
print('{} * {:2} = {}'.format(n ,5, n*5))
print('{} * {:2} = {}'.format(n, 6, n*6))
print('{} * {:2} = {}'.format(n, 7, n*7))
print('{} * {:2} = {}'.format(n, 8, n*8))
print('{} * {:2} = {}'.format(n, 9, n*9))
print('{} * {:2} = {}'.format(n,10, n*10))'''
# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar - considere US$1.00 a R$ 3.27
'''real = float(input('digite qual valor em real tem na carteira: R$'))
dolar = real / 3.27
print('Você tem {} reais e {:.2f} dólares'.format(real, dolar))'''
# Faça um programa que leia a largura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2m quadrados
'''l = float(input('qual a largura sua parede?'))
a = float(input('qual a altura da parede?'))
area = l*a
t = area/2
print('sua parede tem {} de área, vai precisar de {} litros de tinta'.format(area, t))'''
#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
'''preço = float(input('qual é o preço do produto? R$'))
novo = preço - (preço * 5/100)
print('o valor do produto {:.2f}, com 5% de desconto é {:.2f}'.format(preço, novo))'''
# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
'''n = float(input('qual seu salário? R$'))
n1: float = n*15/100
n2 = n+n1
print('seu novo salário com aumento é {:.2f}'.format(n2))'''
# escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''c=float(input('qual a temperatura em Celsius?'))
f= (c*1.8)+32
print('a temperatura em {} °C, é {} °F'.format(c, f))'''
# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado.calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0.15 por km rodado.
km = float(input('quantos Km percorridos?:'))
dias = int(input('dias de uso:'))
valor = (dias * 60)+ (km * 0.15)
print('você percorreu {} Km em {} dias, portanto o custo será de {:.2f}'.format(km,dias,valor))













