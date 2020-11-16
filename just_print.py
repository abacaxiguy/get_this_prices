import functions
from time import sleep

names = ['Processador', 'Placa-Mãe', 'HD', 'Memória', 'Processador', 'Gabinete', 'Teclado', 'Monitor', 'Fonte']

print()
pricesss = functions.get_prices()
for x, i in enumerate(pricesss):

    if x == 8 or x == 2:
        print(names[x] + ': \t\t' + 'R$', i)
    else:
        print(names[x] + ': \t' + 'R$', i)
print()