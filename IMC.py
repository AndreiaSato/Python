# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU ÍNDICE DE MASSA CÓRPOREA (IMC)
# E MOSTRE SEU STATUS, DE ACORDO COMA A TABELA ABAIXO:
# IMC ABAIXO DE 18.5: ABAIXO DO PESO, ENTRE 18.5 E 25: PESO IDEAL, 25 ATÉ 30: SOBREPESO, 30 ATÉ 40: OBESIDADE, ACIMA DE 40: OBESIDADE MÓRBIDA
import math
peso = float(input('qual seu peso (Kg):  '))
altura = float(input('qual sua altura (m):  '))
imc = 0
imc = peso/ (altura ** 2)
print('SEU IMC É {:.1f}, VOCÊ ESTÁ NA FAIXA DE: '.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30 :
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE CUIDADO!!')
elif imc >= 40:
    print('OBESIDADE MÓRBITA! FERROU!!')

