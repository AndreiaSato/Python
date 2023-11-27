# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NUMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO:
while True:
    num = int(input('digite um número: '))
    if num < 0:
        break
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')
    print('QUER VER MAIS UMA TABUADA? DIGITE O NUMERO')