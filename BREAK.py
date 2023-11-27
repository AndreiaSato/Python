'''n = s = 0
while True:
    n = int(input('digite um número  '))
    if n == 999:
        break
    s+=n
#print('A soma dos números vale {}'.format(s))
print(f'A soma vale {s}')'''

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOS 999,
# QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)
n = s = 0
c = 0
while True:
    n = int(input('DIGITE UM NÚMERO INTERIO  '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print (f'VOCÊ DIGITOU {c}')
print(f'A SOMA DOS VALORES É {s} ')





