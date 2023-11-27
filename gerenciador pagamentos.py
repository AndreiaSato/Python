# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
# À VISTA DINHEIRO / CHEQUE: 10% DE DESCONTO, Á VISTA CARTÃO: 5% DE DESCONTO EM ATÉ 2X NO CARTÃO: PREÇO NORMAL, 3X OU MAIS NO CARTÃO: 20% DE JUROS
print('LOJAS AMERICANAS')
preco = float(input('O PREÇO DAS COMPRAS É: R$  '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/ cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opçao?  '))
if opcao == 1:
    total = preco - (preco * 10/ 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas:'))
    parcela = total/totparc
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format (totparc,parcela))
print('Sua compra de R${:.2f} ,vai custar R${:.2f} no final'.format(preco,total))









