

def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':  #-> se a entrada for alfabetica, só espaços vazios ou nulo(enter)
            print(f'ERRO: \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
