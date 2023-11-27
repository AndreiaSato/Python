# ENQUANTO ===  WHILE NOT ===
'''for c in range (1,10):
    print(c)
print('FIM')'''
'''c = 1
while c < 10:
    print(c)
    c = c+1
print('FIM')'''

# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO
# NOVAMENTE ATÉ UM VALOR CORRETO.

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip(). upper()[0]
print('Sexo {}, registrado com sucesso!'.format(sexo))

