# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL,
# NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# A) OS PRIMEIROS CINCO TIMES, B\)NOS ÚLTIMOS 4 COLOCADOS, C)TIMES EM ORDEM ALFABÉTICAS, D) EM QUEPOSIÇÃO ESTÁ O TIME DO SÃO PAULO.

times = 'Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense', 'São Paulo', 'Internacional', 'Athletico-PR', 'Atlético-MG',\
'Fortaleza', 'Cruzeiro', 'Cuiabá', 'Santos', 'Bahia', 'Corinthians', 'Goiás', 'Vasco', 'América-MG', 'Coritiba'
print('-='*15)
print(f'Os cinco primeiro colocados são: {times[0:5]}')
print('-='*15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Em ordem alfabética:{sorted(times)}')
print('-='*15)
print(f'O time São Paulo está na posição {times.index("São Paulo")+1}')
print('-='*15)