# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÉRIO VAI CONTINUAR OU NÃO.
# NO FINAL, MOSTRE: A) QUAL É O TOTAL DE GASTOS NA COMPRA,  B) QUANTOS PRODUTOS CUSATM MAIS DE R$1000, C) QUAL O NOME DO PRODUTO MAIS BARATO:
total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$:'))
    cont = 1
    total = total + preço
    if preço > 1000:
        totmil +=1
    if cont == 1:
         menor = preço
         barato = produto
    else:
         if preço < menor:
            menor = preço
            barato = menor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa'))
print(f'O total da compra é: R${total:.2f}')
print(f'Temos {totmil} custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} e custa {menor:.2f}')