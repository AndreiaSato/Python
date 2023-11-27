#FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
# A) QTS PESSOAS FORAM CADASTRADAS.B) UMA LISTAGEM COM PESSOAS MAIS PESADAS. C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.
pessoas = list()
dados = list()
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('peso: ')))
    if len(dados) == 0:
        mai = men = pessoas [1]
    else:
        if pessoas [1] > mai:
            mai = pessoas [1]
        if pessoas [1] < men:
            men = pessoas [1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = (str(input('Quer continuar? [s/n]')))
    if resp in 'Nn':
       break
print('-==-'*30)
print(f'Os dades foram {dados}')
print(f'Você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {mai}Kg peso de ', end ='')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}]', end ='')
print(f'O menor peso foi de {men} Kg. peso de', end='')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print('-==-'*30)
