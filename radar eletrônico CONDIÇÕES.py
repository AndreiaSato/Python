#escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite
velocidade = float(input('Qual a velocidade atual do carro?'))
if velocidade > 80:
    print('Você excedeu o limite de velocidade!')
    multa = (velocidade-80)*7
    print('Você de ve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com atenção!')