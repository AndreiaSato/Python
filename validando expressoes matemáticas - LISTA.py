# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARENTESES. SEU APLICATIVO DEVERÁ ANALISAR SE
# A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESS ABERTOS E FECHADOS NA ORDEM CORRETA.

expr = str(input('Digite a expressão: '))
pilha = []
for simbolo in expr:
    if simbolo == '(':
       pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')