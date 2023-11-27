# crie um programa que faça o computador jogar jokenpô com
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(1,3)
print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('-='*11)
print('O computador escolheu {}'.format(itens[computador-1]))
print('O jogador jogou {}'.format (itens[jogador-1]))
print('-='*11)
if computador == 1: #PEDRA
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    elif jogador == 3:
        print('COMPUTADOR GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 2: #PAPEL
    if jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 3:
        print('JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 3: #TESOURA
    if jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

