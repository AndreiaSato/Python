# MELHORE O EXERCÍCIO DA PROGRESSÃO ARITMÉTICA PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS.
# O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end ='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS?  '))
print('PROGRESSÃO FINALIZADA COM {} TERMOS MOSTRADOS.'.format(total))

