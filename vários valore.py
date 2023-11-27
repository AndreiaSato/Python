# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999,
# QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)
num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 até parar]:  '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número [999 até parar]:  '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))
