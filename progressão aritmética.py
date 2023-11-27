 # REFAÇA O DESAFIO ANTERIOR, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO WHILE.
'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for c in range (primeiro, decimo + razao , razao):
    print('{}'.format (c), end=" ")
print ('ACABOU')'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print('{} - '.format(primeiro), end ='')
    primeiro += razao
    cont += 1
print('FIM')
