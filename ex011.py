#calculo de tinta para pintar uma parede

largura = float(input('informe o largura da parede: '))
comprimento = float(input('informe o comprimento da parede: '))

print(f'sua parede possui uma área de {largura*comprimento}m²')
print(f'para pintar sua parede voce vai precisar de {(largura*comprimento)/2:.2f} litros de tinta')