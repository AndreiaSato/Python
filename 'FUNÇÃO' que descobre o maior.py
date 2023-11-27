#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁIOS PARÃMETROS COM VALORES INTEIROS. SEU PROGRAMA
#TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.


from time import sleep
def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f' {valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'  Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#programa principal
maior(10, 5, 2)
maior(9, 3, 1)
maior(0, 2)
maior(1, 2)