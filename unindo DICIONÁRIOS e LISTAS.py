# CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO E
# TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE: A) QUANTAS PESSOAS FORAM CADASTRADAS, B) A MÉDIA DE IDADE C) UMA LISTA COM AS MULHERES
# D) UMA LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:  [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digitar M ou F!')
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
         resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
         if resp in 'SN':
            break
         print('ERRO! Responda S ou N.')
    if resp == 'N':
            break
    print(pessoa)
print('+'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print("as mulheres cadastradas foram: ", end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
       print(f'{p["nome"]} ', end='')
print()
print(f'Lista das pessoas que estão acima da média:')
for p in galera:
    if p['Idade']>= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()

print('+'*35)





