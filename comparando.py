#ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS MOSTRANDO NA TELA UMA MENSAGEM :
# - o PRIMEIRO VALOR É MAIOR - o SEGUNDO VALOR É MAIOR - nÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS:
n1 = int(input(' Digite um numero inteiro:'))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('o PRIMEIRO VALOR é o MAIOR.')
elif n2 > n1:
    print('o SEGUNDO VALOR  é o MAIOR.')
else:
    print('os dois valores são IGUAIS')

