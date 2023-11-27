#SORTEIOS
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome escolhido
'''import random
p = str(input('Digite o nome do primeiro aluno:'))
s = str(input('Digite o nome do segundo aluno:'))
t = str(input('Digite o nome do terceiro aluno:'))
q = str(input('Digite o nome do quarto aluno:'))
lista = [p,s,t,q]
print('dentre os alunos {} {} {} {} o escolhido é {}'.format (p,s,t,q,random.choice(lista)))'''

# o mesmo professor do desafio anterior quer sortear a ordem de apresntação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada
import random
p = str(input('primeiro aluno'))
s = str(input('segundo aluno'))
t = str(input('terceiro aluno'))
q = str(input('quarto aluno'))
lista = [p,s,t,q]
random.shuffle(lista)
print('A ordem dos alunos será')
print (lista)

