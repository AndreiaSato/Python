#CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).DEPOIS DISSO, VOCÊ DEVE MOSTRAR,
#PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.

palavra = ('NICOLE','MARIA','BEATRIZ','STEFANIE','PAULA','CAMILA','PATRICIA','ANA','SOFIA','VITORIA')
for p in palavra:
    print(f'\n No nome {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')

