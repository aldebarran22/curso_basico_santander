"""
Operadores relacionales y lógicos
"""

num = 15
ini = 10
fin = 50

if num >= ini and num <= fin:
    print('dentro del intervalo')
else:
    print('fuera del intervalo')

if ini <= num <= fin:
    print('dentro del intervalo')
else:
    print('fuera del intervalo')

if num < ini or num > fin:
    print('fuera del intervalo')
else:
    print('dentro del intervalo')

if not (num >= ini and num <= fin):
    print('fuera del intervalo')
else:
    print('dentro del intervalo')

# Imprimir el menor de dos números teniendo en cuenta si son iguales:
n1 = 12
n2 = 34

if n1 < n2:
    print('El menor es ',n1)

    if n1 % 2 == 0:
        print('n1 es par')

elif n2 < n1:
    print('El menor es ', n2)

else:
    print('son iguales')

