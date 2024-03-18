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

