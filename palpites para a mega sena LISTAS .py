# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR D MEGA SENA A CRIAR PALPITES. O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERAO GERADOS
# E VAI SORTEAR 6 NUMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA COMPOSTA
print('+'*30)
print( '     JOGO MEGA SENA')
print('+'*30)
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie>:  '))
tot = 1
while tot <= quant:
    from random import randint
    cont = 0
    while True:
        num = randint (1,60)
        if num not in lista:
            lista.append (num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
for i,l in enumerate (jogos):
    print(f'Jogo {i+1}: {l}')
print("BOA SORTE!!")
