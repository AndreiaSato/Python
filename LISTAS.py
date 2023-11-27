'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate (valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''valores = list()
for cont in range (0,5):
    valores.append(int(input('Digite um valor  ')))
for c,v in enumerate (valores):
    print(f'Na posição {c} encontrei o valor {v}!')
    
print('Cheguei ao final da lista.')'''

#FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE O MAIOR E O MENOR VALOR DIGITADO
# E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA

listanum = []
maior = 0
menor = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum [c]
    else:
        if listanum [c] > maior:
            maior = listanum[c]
        if listanum [c] < menor:
            menor = listanum[c]
print('-='*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end=(' '))
for i,v in enumerate (listanum):
    if v == maior:
        print(f'{i}...',end='')
print(f'o menor valor digitado foi: {menor} nas posições ',end=(' '))
for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end=(''))
print()
