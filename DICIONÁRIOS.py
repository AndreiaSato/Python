# TUPLAS()  /  LISTAS []  /  DICIONÁRIOS {}
# values (valores) / keys (chaves)   / items (valores e chaves)
pessoas = {'nome': 'Andréia', 'sexo': 'F','idade': 47}
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range (0,3):
    estado ['uf']= str(input('Unidde Federativa: '))
    estado ['sigla']= str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # copiar a lista [:] não serve para dicionário, tem que ser copy()
print(brasil)
