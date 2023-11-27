# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR
# SE O USUÁRIO QUER OU NÃO CONTINUAR. NO FINAL MOSTRE: A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS  B)QUANTOS HOMENS FORAM
# CADASTRADOS C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.
tot18 = toth = totm = 0
while True:
    idade = int(input('Qual idade: '))
    sexo = ' '
    while sexo not in 'M/F':
        sexo = str(input('M/F ')). strip().upper()[0]
    if idade >= 18:
        tot18 +=1
    if sexo =='M':
        toth += 1
    if sexo == 'F' and idade <20:
        totm +=1
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N] ')).strip(). upper() [0]
    if resp == 'N':
        break
print('* Total de pessoas com mais de 18 anos: {}'.format (tot18))
print('* Total de pessoas do sexo masculino: {}'.format(toth))
print('* Total de mulheres com menos de 18 anos é: {}'.format(totm))