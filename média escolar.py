# CRIE UM PROGRAMA QUE LEI DUAS NOTAS DE UM ALUNO E CALCULE SU MÉDI, MOSTRANDO UMA MENSAGEM NO FNAL, DE ACORDO COM A MÉDIA ATINGIDA:
# - MÉDIA ABAIXO DE 5.0: REPROVADO - MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO - MÉDIA 7.0 OU SUPERIOR: APROVADO
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print('QUE PENA, VOCÊ ESTÁ REPROVADO! sua média é {:.1f}'.format(m))
elif m >= 5.0 and m < 6.9:
    print('VOCÊ ESTÁ EM RECUPERAÇÃO, sua média é {:.1f}'.format(m))
else:
    print('PARABÉNS! VOCÊ FOI APROVADO!!')
