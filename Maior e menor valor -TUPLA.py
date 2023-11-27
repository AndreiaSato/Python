#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS
# GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA
from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram {num}')
print(f'O maior valor sorteado é: {max(num)}')
print(f'O menor valor é: {min(num)}')