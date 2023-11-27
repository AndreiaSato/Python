# INTERACTIVE HELP: help() -/
# DOCSTRINGS

def contador(i, f, p):
    """
     -> Faz um contagem e  mostra na tela:
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f :
        print(f'{c}  ', end='')
        c += p
    print('FIM')
contador(2,10,2)
help(contador)

#PARÂMETRO OPCIONAL
def somar (a=0, b=0, c=0):

    s = a+b+c
    print(f'--> A soma vale {s}')
somar(3,5)

#ESCOPO DE VARIÁVEIS
def teste(b):
#escopo local
    b+=4
    c=2
    print(f'* A dentro vale {a}')
    print(f'* B dentro vale {b}')
    print(f'* C dentro vale {c}')

#escopo global
a=5
teste(a)
print(f'--> A fora vale{a}')

#RETORNO DE VALORES
def somar (a=0,b=0, c=0):
    s = a+b+c
    return s

r1 = somar(3,2,5)
r2 = somar(1,7)
r3 = somar(4)
print(f'--> Meus cálculos deram: {r1}, {r2}, {r3}')



