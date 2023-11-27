# ROTINA: criar uma função muito usável, um comando novo..., personalizado --- Def ---
#exemplo:
def titulo (txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

#Programa Principal
titulo('  Curso em Vídeo  ')
titulo(' Python é muito Bom ')
titulo(' Andréia vai ficar craque!')

print('='*30)

def soma (a, b):
    s = a + b
    print(s)
soma(3, 4)
soma(4, 4)
soma(3, 3)

print('='*30)

def soma(a,b):
    print(f'A={a} e B{b}')
    s = a+b
    print(f'A soma A + B = {s}')
soma(1,2)
soma(6,5)
soma(8,9)

print('='*30)

def contador(* num):


    print('='*30)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 0, 2]
dobra(valores)
print(valores)


