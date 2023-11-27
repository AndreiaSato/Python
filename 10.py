# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO
'''cidade = str(input('digite em qual cidade você nasceu:')).strip()
print(cidade[:5].upper() == 'SANTO')'''

# crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome

'''nome = str (input('QUAL SEU NOME?:'))
print(' SEU NOME TEM SILVA?: {}'.format('silva'in nome.lower()))'''

# faça um programa que leia uma frase pelo teclado emostre quantas vezes aparece a letra 'A',
# em que posição ela aparece a primeira vez e em que posição ela aparece última vez
'''frase = str(input('DIGITE UMA FRASE:')).upper().strip()
print('A LETRA A APARECE {} VEZES'.format(frase.count('A')))
print('a primeira letra a aparece na {} posição'.format(frase.find('A')+1))
print('a ultima posição da letra A é a {} '.format(frase.rfind('A')+1))'''

# faça um programa que leia O nome completo de ima pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = str(input('digite seu nome completo:')).strip()
n = nome.split()
print('seu primeiro nome é {}'.format(n[0]))
print('seu segundo nome é {}'.format(n[len(n)-1]))
