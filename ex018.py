#Cálculo do seno, cosseno e tangente
import math

ang = float(input(f'informe o angulo em que você deseja informações: '))
ang = math.radians(ang)
print(f'SENO de {ang}° = {math.sin(ang):.2f}')
print(f'COSSENO de {ang}° = {math.cos(ang):.2f}')
print(f'TANGENTE de {ang}° = {math.tan(ang):.2f}')