# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Qual ano você quer consultar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 !=0 or ano %400 ==0:   #divisível por 4, não divisível por 100 ou divissível por 400
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print ('o ano {}, não é BISSEXTO.'.format (ano))
 