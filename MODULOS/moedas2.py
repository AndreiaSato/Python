#CRIE UM MODULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO(),. FAÇA TAMBÉM UM PROGRAMA
# QUE IMPORTE ESSE MODULO E USE ALGUMAS DESSAS FUNÇÕES

'''import moeda
p = float(input('Digite o preço:R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando R${p} em 20%, temos R${moeda.aumentar(p,20)}')
print(f'Diminuindo R${p} em 10%, temos R${moeda.diminuir(p,10)}')'''

# AGORA ADAPTANDO O EXERCÍCIO ANTERIOR, CRIE UMA FUNÇÃO CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS NÚMEROS COMO UM VALOR MONETÁRIO
# FORMATADO

import moeda2
p = float(input('Digite o preço: '))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}')
print(f'Aumentando {moeda2.moeda(p)} em 20%, temos {moeda2.moeda(moeda2.aumentar(p,20))}')
print(f'Diminuindo {moeda2.moeda(p)} em 10%, temos {moeda2.moeda(moeda2.diminuir(p,10))}')
