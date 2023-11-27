# CRIE UM PROGRAMA QUE DECLARE UMA MATRIZ DE DIMENSÃO 3X3 E PREENCHA COM VALORES LIDOS PELO TECLADO.
# NO FINAL, MOSTRE NA TELA, COM A FORMATAÇÃO CORRETA.

matriz = [[0,0,0], [0,0,0],[0,0,0]]
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz [l][c]}]', end='')
    print()
