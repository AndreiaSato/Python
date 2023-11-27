# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
# E QUAL FOI O MAIOR E O MENOR VALOR LIDO. O PROGRMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma/quant
print('A Você digitou {} números e a média foi {}'.format(quant,media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))
print('ACABOU!')