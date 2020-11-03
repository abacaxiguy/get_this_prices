import functions
from time import sleep

names = ['Processador', 'Placa-Mãe', 'HD', 'Memória', 'Fonte', 'Gabinete', 'Teclado', 'Monitor']

print()
pricesss = functions.get_prices()
for x, i in enumerate(pricesss):
    if x == 2 or x == 4:
        print(names[x] + ': \t\t' + 'R$', i)
    else:
        print(names[x] + ': \t' + 'R$', i)
print()