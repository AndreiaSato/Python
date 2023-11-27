# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS:
# * O NOME DE UM JOGADOR E QTS GOLS ELE MARCOU. O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE
# ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.

def ficha (jogador ='<desconhecido>', gol = 0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')





#programa principal
n = str(input('Nome do jogador:  '))
g = str(input('Numero de gols:  '))
if g.isnumeric():
    go= int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
