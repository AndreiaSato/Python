# Refaça o exercicio anterior (Gua19) dos triângulos, acrescentando o ecurso de mostrar que tipo de triângulo será formado
# EQUILÁTERO: todos os lados iguais, ISÓCELES: dois lados iguais e um diferente, ESCALENO: todos os lados diferentes
a = float(input(' Digite o primeiro segmento:  '))
b = float(input('Digite um segundo segmento:  '))
c = float(input('Digite um terceiro segmento:  '))
if a < b+c and b< a+c and c< a+b:
    print('Os segmentos podem formar um triângulo ', end = '')
    if a==b and b==c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print ('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO!')

