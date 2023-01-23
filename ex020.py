#embaralhando nomes
import random
lista = []

for c in range (1,5):
    lista.append(input(f'informe o nome do {c}° aluno: '))

random.shuffle(lista)
print(f'a ordem de apresentação será {lista}')

