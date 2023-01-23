#Quebrando um numéro

import math

valor = float(input('informe um valor: '))
#maneira 1
print(f'a parte inteira do valor que voce digitou é {int(valor)}')

#maneira 2
print(f'a parte inteira desse do valor que voce digitou é {math.trunc(valor)}')