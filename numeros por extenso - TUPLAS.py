#CRIE UM PROGRAMA QUE TENHA UMA DUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO A VINTE.
#PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO.

cont = 'zero', 'um', 'dois', 'três','quatro','cinco',' seis','sete','oito','nove','dez','onze','doze','treze',\
'quatorze','quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte'
while True:
    num = int(input('Digite um número inteiro entre 0 a 20:  '))
    if 0 <= num <=20:
        break
    print('Digite novamente!')
print(f'Você digitou o número {cont[num]}')
