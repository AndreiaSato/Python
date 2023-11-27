#DENTRO DO PACOTE UTILIDADESCEV, TEMOS UM MÓDULO CHAMADO DADO. CRIE UMA FUNÇÃO CHAMADA LeiaDinheiro() QUE SEJA CAPAZ DE
# FUNCIONAR COM A FUNÇÃO INPUT(), MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJAM MONETÁRIOS.


from moeda5.utilidadescv import moeda
from moeda5.utilidadescv import dado
p = dado.leiadinheiro ('Digite o preço:R$ ')

moeda.resumo(p)

