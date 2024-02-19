"""
Resolver ecuaciones de segundo grado.
"""

import math

# from math import sqrt

a, b, c = 1, 2, 3  # a = 1, b = 5, c = 4

raiz = b**2 - 4 * a * c

if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2 * a)
    x2 = (-b - math.sqrt(raiz)) / (2 * a)
    print("x1:", x1, "x2:", x2)
else:
    print("No hay solución")
