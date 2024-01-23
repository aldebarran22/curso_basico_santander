"""
Resolver una ecuacion de 2º grado con Python
ax^2 + bx + c = 0
x1 y x2
"""

import math

# inicializar variables:
a, b, c = 1, 5, 4  # a = 1 b = 5 c = 4
# a,b,c=1,2,3

raiz = b**2 - 4 * a * c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2 * a)
    x2 = (-b - math.sqrt(raiz)) / (2 * a)

    print("x1:", x1, sep="")
    print(f"x2:{x2}")
else:
    print("No se puede calcular")
