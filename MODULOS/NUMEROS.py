from uteis import numeros  #criado por mim e salvo no arquivo separado

#programa principal
num = int(input('Digite um valor  '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é { fat } ')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
