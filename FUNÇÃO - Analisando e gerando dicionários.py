#FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS
# SEGUINTES INFORMAÇÕES: * QUANTIDADE DE NOTAS * A MAIOR NOTA * A MENOR NOTA * A MÉDIA DA TURMA * A SITUAÇÃO (OPCIONAL)

def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situaçao da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r ['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#programa principal
resp = notas(9.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)