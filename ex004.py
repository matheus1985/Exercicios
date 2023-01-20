#Dissecando uma variavel

a = input('digite algo: ')
if a.isnumeric():
    a = int(a)
    print(f'voce digitou um elemento do tipo {type(a)}')
else:
    print(f'voce digitou um objeto do tipo {type(a)}')
    print(f'Só possui espaços: {a.isspace()}')
    print(f'é um numero: {a.isnumeric()}')
    print(f'é alfabetico: {a.isalpha()}')
    print(f'é maiuscula: {a.isupper()}')
    print(f'é minuscula: {a.islower()} ')
    print(f'esta capitalizada: {a.istitle()}')