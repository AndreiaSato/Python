# CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA. NO FINAL,
# MOSTRE UMA LINGUAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR

frutas = ('banana','R$4,50','abacaxi','R$6,00','maçã','R$7,60','mertiliio','R$12,00','morangos','R$8,00','pêra','R$7,50','uvas',
          'R$8,00','melancia','R$10,00')
print('-='*20)
for cont in range (0,len(frutas),2):
    print(f'A fruta {frutas[cont]}: {frutas[cont +1]}')
print('-='*20)
