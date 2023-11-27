# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E
# OUTRO CHAMADO SHOW, QUE SEERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO NA TELA O PROCESO DE CÁLCULO


def fatorial (n, show=False):
    """
    --> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um numero n.

    """
    f = 1
    for c in range (n, 0, -1):
        if show:
          print(c , end='')
          if c > 1:
            print(' x ' , end='')
          else:
            print(' = ' , end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
