"""ecuacion.py

Resolver la ecu de 2 grado
"""

import math

a,b,c = 1,2,3

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)

    # f-string
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
else:
    print('No hay solución ...')
