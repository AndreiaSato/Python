# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA.
# CASO O NÚMERO JÁ EXISTE LÁ DENTRO, ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.
numero = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('--'*30)
numero.sort()
print(f'Você digitou os valores {numero}')


