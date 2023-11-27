# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE,
# SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, SE É A HORA EXATA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO.
# SEU PROGRAMA DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano de seu nascimento:  '))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido  em {}'.format(ano))


