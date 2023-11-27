#REESCREVA A FUNÇÃO leiaInt() QUE FIZEMOS ANTERIORMENTE, INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM NÚMERO DO TIPO
#INVÁLIDO. APROVEITE E CRIE TBM UMA FUNÇÃO leiaaFloat() COM A MESMA FUNCIONALIDADE.

def leiaInt(msg):
    while True:
        try:
         n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número Real válido: ')   # não pode digitar , tem que ser .
            return 0
        else:
            return n


n1 = leiaInt('Digite um número:  ')

n2 = leiaFloat('Digite um número real: ')
print(f'O número interiro digitado foi {n1} e o número real {n2}')