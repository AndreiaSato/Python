# MELHORE O JOGO DO DESAFIO ANTERIOR (12) ONDE O COMPUTADOR VAI PENSAR EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR
# VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint (0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('você ganhou!')
            v += 1
        else:
            print('você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
print('Vamos jogar novamente?')
print (f'Você venceu {v}')

