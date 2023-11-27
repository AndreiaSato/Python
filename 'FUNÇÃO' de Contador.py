#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIM E PASSO. SEU PROGRAMA
#TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA: A) DE 1 ATÉ 10, DE 1 EM 1 / B) DE 10 ATÉ 0, DE 2 EM 2 / UMA CONTAGEM PERSONALIZADA

from time import sleep
def contador(i, f, p):
    if p < 0 :
        p *= -1
    if p == 0:
        p*1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.0)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} - ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
             print(f'{cont} - ', end='', flush=True)
             sleep(0.5)
             cont -= p
        print('FIM')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)
print('=' * 40)
