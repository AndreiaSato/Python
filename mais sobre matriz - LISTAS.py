# APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL: A) A SOMA DE TODOS OS VALORES PARES DIGITADOS,
# B) A SOMA DOS VALORES DA TERCEIRA COLUNA, C) O MAIOR VALOR DA SEGUNDA LINHA

matriz = [[0,0,0], [0,0,0],[0,0,0]]
somapares = maior = somacoluna = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}],[{c}]: '))
print('+'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz [l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:
            somapares += matriz[l][c]
    print()
print('+'*30)
print(f'A soma dos valores pares é {somapares}')
for l in range (0,3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for c in range (0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz [1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
