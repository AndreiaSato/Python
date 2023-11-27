from criamenu.lib.interface import *
from criamenu.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resp == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
        print('Opçao 01')
    elif resp == 2:
        # opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME:  '))
        idade = leiaInt('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Saindo do Sistema... Até Logo!')
        break
    else:
        print('Erro! Digite uma opçâo válida!')