import functions
from time import sleep

print()
pricesss = functions.get_prices()
for x, i in enumerate(pricesss):
    print('R$', i)
print()