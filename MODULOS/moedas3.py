#MODIFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO MOEDAS2 PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, INFORMANDO SE O
# VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO MOEDA2

import moeda3
p = float(input('Digite o preço: '))
print(f'A metade de {moeda3.moeda(p)} é {moeda3.metade(p, True)}')
print(f'O dobro de {moeda3.moeda(p)} é {moeda3.dobro(p, True)}')
print(f'Aumentando {moeda3.moeda(p)} em 20%, temos {moeda3.aumentar(p,20, True)}')
print(f'Diminuindo {moeda3.moeda(p)} em 10%, temos {moeda3.diminuir(p,10, True)}')
