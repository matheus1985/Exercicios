from math import hypot

co = float(input(f'informe o valor do cateto oposto: '))
ca = float(input(f'informe o valor do cateto adjacente: '))
print(f'o valor da hypotenus é {hypot(ca, co):.2f}')