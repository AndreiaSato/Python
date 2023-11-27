# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER,
# MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.


nu = int(input('DIGITE UM NÚMERO:'))
resultado = nu % 2
if resultado == 1:
    print ('Você digitou um número ímpar!')
else:
    print('o número é PAR')