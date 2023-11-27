# VARIÁVEIS COMPOSTA --> LISTAS DENTRO DE OUTRA LISTA
'''test = list()
test.append('Andréia')
test.append(47)
print(test)
galera = list()
galera.append(test[:])
test[0] = 'Gabriel'
test[1] = 42
galera.append(test)
print(galera)'''

'''galera = [['Andreia',47], ['Nicole',13], ['João', 24]]
print(galera)
print(galera[2][0])
print(galera[0][0])

for p in galera:
    print(p[0])
    
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

totmais = totmenos = 0
galera = list()
dado = list()
for c in range (0,3):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade:  ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmais +=1
    else:
        print(f'{p[0]}, é menor de idade.')
        totmenos += 1
print(f'Temos {totmais} maiores  e {totmenos} menores de idade')