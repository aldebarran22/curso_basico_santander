"""
Resolver ec. de 2º en python
ax^2 + bx + c = 0
"""
import math

a = 1
b = 2
c = 3

raiz = b**2 - 4*a*c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2 * a)
    x2 = (-b - math.sqrt(raiz)) / (2 * a)
    print("x1:",x1)
    print(f"x2: {x2}")
else:
    print('Raiz negativa')