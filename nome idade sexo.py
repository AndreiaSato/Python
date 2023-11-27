# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE: A MÉDIA DE IDADE DO
# GRUPO, QUAL É O NOME DO HOMEM MAIS VELHO E QUANTAS MULHERES TÊM MENOS DE 20 ANOS.
soma = 0
media = 0
maioridadehomem = 0
nomemaisvelho = ' '
totmulher = 0
for n in range (1,5):
    nome = str(input('qual o {}º nome:'.format(n)))
    idade = int(input('qual a {}ª idade: '.format(n)))
    sexo = str(input('qual o {}º sexo [M/F]: '.format(n)))
    soma += idade # serve para qualquer operador
    if n == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A média da idade do grupo é {}'.format(media))
print('A idade do homem mais velho é {} e se chama {}'.format (maioridadehomem,nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))


