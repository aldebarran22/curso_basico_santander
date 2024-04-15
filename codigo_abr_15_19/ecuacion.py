"""
Calcular ecuaciones de 2 grado en Python
ax^2 + bx + c = 0
"""

import math

# Inicialización múltiples:
a,b,c = 1,2,3

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)
    print("x1:",x1,"x2:",x2)

    #f-string
    print(f"x1: {x1}, x2: {x2}")
else:
    print('No hay solución')

