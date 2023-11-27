# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O
# VALOR A SER SACADO(NUMERO INTERIO) E O PROGRAMA VAI INFORMAR QUANTAS CÉLULAS DE CADA VALOR SERÃO ENTREGUE.
# * CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50 R$20, R$10 A R$1.
valor = int(input('Que valor você quer sacar?: R$'))
total = valor
totced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
