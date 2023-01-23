#sorteando nomes

import random
lista = []

for c in range(1,5):
    lista.append(input(f'informe o {c}° nome para o sorteio: '))

print(f'o nome sorteado foi {random.choice(lista)}')