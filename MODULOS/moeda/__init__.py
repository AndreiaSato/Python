#CRIE UM MODULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO(),. FAÇA TAMBÉM UM PROGRAMA
# QUE IMPORTE ESSE MODULO E USE ALGUMAS DESSAS FUNÇÕES


def aumentar(preço, taxa):
   res =  preço +(preço * taxa / 100)
   return res

def diminuir(preço, taxa):
    res = preço - (preço * taxa /100)
    return res

def dobro(preço):
    res = preço * 2
    return res

def metade(preco):
    res = preco / 2
    return res

