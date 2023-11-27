# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UMA PROGRMA QUE LEIA O ANOS DE NASCIMENTO DE UM ATLETA E MOSTRE
# SUA CATEGORIA, DE ACORDO COM A IDADE: - ATÉ 9 ANOS; MIRIM, -ATÉ 14 ANOS: INFANTIL, - ATÉ 19 ANOS: JÚNIOR,
# - ATÉ 25 ANOS: SÊNIOR, - ACIMA DE 25 ANOS: MASTER
from datetime import date
atual = date.today(). year
nascimento = int(input('Qual o ano de seu nascimento?  '))
idade = atual-nascimento
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('categoria MIRIM')
elif idade <=14:
    print('categoria INFANTIL')
elif idade <= 19:
    print('categoria JÚNIOR')
elif idade <= 19:
    print('categoria SÊNIOR')
elif idade <= 25:
    print ('categoria MASTER')


