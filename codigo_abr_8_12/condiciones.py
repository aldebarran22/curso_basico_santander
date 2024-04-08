"""
Condiciones en Python. Comprobar si una var. está o no dentro de un 
intervalo.
"""

ini = 10
fin = 50
num = 12
if num >= ini and num <= fin:
    print(f'{num} está dentro del intervalo')
else:
    print(' no está en el intervalo')

if  ini <= num <= fin:
    print(f'{num} está dentro del intervalo')
else:
    print(' no está en el intervalo')

if not (ini <= num <= fin):
    print(' no está en el intervalo')
else:
    print(f'{num} está dentro del intervalo')

if num < ini or num > fin:
    print(' no está en el intervalo')
else:
    print(f'{num} está dentro del intervalo')