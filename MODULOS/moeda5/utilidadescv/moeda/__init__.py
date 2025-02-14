def aumentar(preco =0, taxa=0, format=False):
    '''
    --> calcular o aumento de um determinado preço retornando
    o resultado com ou sem formatação
    :param preco: o preco que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param format: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)

def diminuir(preco = 0, taxa = 0, format=False):
    res = preco - (preco * taxa /100)
    return res if format is False else moeda(res)

def dobro(preco = 0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)

def metade(preco = 0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxaa=10,taxar=5):    # TAXAA - taxa aumento / TAXAR - taxa de redução
    print('='*40)
    print('RESUMO DO VALOR'. center(30))  # center(30) - indica centralizado em 30 caracteres
    print('='*40)
    print(f'Preço analisado: \t    {moeda(preco)}')
    print('='*40)
    print(f'O Dobro do preço: \t    {dobro(preco, True)}')
    print('='*40)
    print(f'A Metade do preço: \t    {metade(preco, True)}')
    print('='*40)
    print(f'Com a {taxaa}% de aumento:\t{aumentar(preco, taxaa, True)}')
    print(f'Com a {taxar}% de redução:\t{diminuir(preco,taxar,True)}')
    print('='*40)
