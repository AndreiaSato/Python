# IF:/ ELIF:/  ELSE: /
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA,
# O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE
# EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO
valor = float(input('Qual o valor da casa desejada?'))
salario = float(input('Qual o salário do comprador?'))
anos = int(input('Tempo para quitação da compra:'))
prestacao = valor/(12*anos)
if prestacao <= salario*30/100:
    print('Para uma casa de R${:.2f},em {} anos, a prestação será de R${:.2f},Seu empréstimo foi CONCEDIDO!'.format(valor,anos,prestacao))
else:
    print('que pena, seu empréstimo NÃO FOI APROVADO!')
