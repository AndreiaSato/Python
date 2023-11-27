# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.
'''from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(0.5)
print('POW')'''
# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50
'''for n in range(1, 51):
    if n % 2 == 0:
        print (n, end=' ')
print('-- ESTES NUMEROS SÃO PARES!')'''
# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS QUE SÃO MÚLTIPLOS DE TRÊS E QUE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.
'''soma = 0
cont = 0
for num in range (1, 501, 2):
    if num %3 == 0:
        cont = cont + 1
        soma = soma + num
print ('A soma de todos os {} valores solicitafos é {}.'.format (cont, soma))'''
# REFAÇA O EXERCÍCIO DA TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
'''num = int(input('digite um número: '))
for c in range (1,11):
    print('{} x {} = {}'.format(num,c, num*c))'''
# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE - O
'''soma = 0
cont = 0
for c in range (1,7):
    num = int(input('digite o {} valor:'.format(c)))
    if num % 2 == 0:
         soma = soma + num
         cont = cont + 1
print('Você digitou {} numeros  PARES e a soma foi {}'.format(cont,soma))'''
# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO:
'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for c in range (primeiro, decimo + razao , razao):
    print('{}'.format (c), end=" ")
print ('ACABOU')'''
#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO
'''num = int(input('DIGITE UM NUMERO INTEIRO:  '))
tot = 0
for c in range (1,num,+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot +1
    else:
        print('\033[31m', end='')
    print ('{}'.format (c), end=' ')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print(' E por isso ele NÃO É PRIMO')
else:
    print('E por isso ele é PRIMO')'''
# CRIE UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS. EXEMPLOS DE PALÍNDROMOS

 # (MANIPULANDO TEXTOS - ANÁLISES com: len()-"comprimento", count()-"contar", find()-"encontrar"
# TRANSFORMAÇÕES: com replace() -"trocar/substituir", upper()-"maiúsculas" , lower()- "minúsculas",
# capitalize()-"tudo em minusculos e a primeira letra em maiusculas", title()-"parecido com capitalize, mas todas as primeiras
# letras após espaço", strip()-"remove espaços inúteis" - rstrip (espaços do lado direito será removido) - lsttrip(remove
# os da esquerda),
# DIVISÃO: split()- gera uma lista separados pelos espaços,
# JUNÇÃO: join()- '-' coloca um traço nos espaços)

'''frase = str(input('DIGITE UMA FRASE:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]
print('O INVERSO DE {} É {}'. format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO TEMOS UM PALÍMETRO!')'''
# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A
# MAIORIDADE E QUANTAS JÁ SÃO MAIORES
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('EM QUE ANO A {}ª PESSOA NASCEU? '.format(pess)))
    idade = atual - nasc
    print(''.format())
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print('AO TODO TIVEMOS {} PESSOAS MAIORES DE IDADE'.format(totmaior))
print('AO TODO TIVEMOS {} PESSOAS MENORES DE IDADE'.format(totmenor))























