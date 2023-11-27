#CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO
# EM PYTHON. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking = list()
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print(ranking)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com: {v[1]}')
    sleep(1)