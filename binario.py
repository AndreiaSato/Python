# ESCREVA UM PROGRAMA EM PYTHON QUE LEIA UM NUMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOHER QUAL SERÁ A BASE DE CONVERSÃO:
# 1 PARA BINÁRIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL.
n = int(input('Escolha um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 [ converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format (n, bin(n)[2:]))
elif opção ==2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opção ==3:
    print('{} convertido para HEXADECIMAL é igual a {}'. format (n, hex(n)[2:]))
else:
    print('Opção errada. Tente novamente')

