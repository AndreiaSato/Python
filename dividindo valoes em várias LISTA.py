# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO
# CONTER APENAS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número:  ')))
    resp = str(input('Quer continuar?[s/n]: '))
    if resp in 'Nn':
        break
for i,v in enumerate (num):
    if v %2 == 0:
        pares.append(v)
    elif v%2 ==1:
        impares.append(v)
print('=-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
print('=-='*30)