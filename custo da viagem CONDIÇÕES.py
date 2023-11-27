# Desenvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# KM para viagens de até 200KM e R$0,45 para viagens mais longas.
distancia = float(input('Qual é a distância de sua viagem?'))
print ('Você está prestes a começar uma viagem de {} KM'.format(distancia))
if distancia <= 200:
    print('Pague R${:.2f}'.format(distancia*0.50))
else:
    print('Pague R${:.2f}'.format(distancia*0.45))

