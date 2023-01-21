#aluguel de carros

print('ALUGUEL DE CARROS')
print('-='*12)
print('diária = R$60,00')
print('km rodado = R$0,15')
diaria = 60
km = 0.15
print('-='*12)

tempo = int(input('informe a quantidade de dias de aluguel: '))
dist = float(input('informe quantos KM voce vai precisar: '))

print(f'{tempo} dias de aluguel rodando {dist} km voce vai pagar R${(tempo*diaria)+(dist*km):.2f}')