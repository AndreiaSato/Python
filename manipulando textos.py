#TOCANDO MUSICA MP3
# Faça um programa em Python que abra e repruduza o áudio de um arquivo MP3
'''import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame. mixer.music.play()
pygame.event.wait()'''

 # MANIPULANDO TEXTOS - ANÁLISES com: len()-"comprimento", count()-"contar", find()-"encontrar"
# TRANSFORMAÇÕES: com replace() -"trocar/substituir", upper()-"maiúsculas" , lower()- "minúsculas",
# capitalize()-"tudo em minusculos e a primeira letra em maiusculas", title()-"parecido com capitalize, mas todas as primeiras
# letras após espaço", strip()-"remove espaços inúteis" - rstrip (espaços do lado direito será removido) - lsttrip(remove
# os da esquerda),
# DIVISÃO: split()- gera uma lista separados pelos espaços,
# JUNÇÃO: join()- '-' coloca um traço nos espaços

'''frase = 'sou muito feliz'
print(frase.split())'''

# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com todas as minúsculas
# quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome

nome = str(input('DIGITE SEU NOME:')).strip()
print('SEU NOME EM MAIÚSCULAS É {}'.format (nome.upper()))
print('SEU NOME EM MINÚSCULAS É {}'.format(nome.lower()))
print('SEU NOME TEM AO TODO {} LETRAS'.format(len(nome)-nome.count(' ')))
#print('SEU PRIMEIRO NOME TEM {} LETRAS'.format(nome.find(' ')))
separa = nome.split()
print('SEU PRIMEIRO NOME É {} E TEN {} LETRAS'.format(separa[0],len (separa[0]))














