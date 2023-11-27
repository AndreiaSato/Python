# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO)
# E MOSTRE A  ÁREA DO TERRENO.
print('CONTROLE DE TERRENOS')
print('='*20)
def med (l, c):
    area = l * c
    print( f'a área é {area}')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
med(l,c)
