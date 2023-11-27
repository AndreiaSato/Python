# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARÂMETRO O ANO DE UMA PESSOA, RETORNANDO UM
# VALOR LITERAL, INDICANDO SE UMA PESSOA TEM VOTO NEGADO / OPCIONAL / OBRIGATÓRIO NAS ELEIÇÕES


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos : NÃO VOTA!'
    elif 16 <= idade <18 or idade >65: #idade menor ou igual a 16 e maior que 65
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

#programa principal

nasc = int(input('Em que ano você nasceu?  '))
print(voto(nasc))

