#analisador de textos

nome = input("informe seu nome: ").strip()
nome = nome.split()
nome = ' '.join(nome)
print('analisando seu nome...')
print(f'Seu nome em maiúscula é {nome.upper()} ')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome com apenas a primeira letra maiúscula é {nome.capitalize()}')
print(f'Seu nome possui {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome possui {len(nome.split()[0])} letras')
