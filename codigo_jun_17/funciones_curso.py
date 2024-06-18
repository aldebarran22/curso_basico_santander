"""
Ejemplos de funciones
"""

import math

raiz = b**2 - 4 * a * c
if raiz > 0:
    x1 = (-b + math.sqrt(raiz)) / (2 * a)
    x2 = (-b - math.sqrt(raiz)) / (2 * a)
    print("x1: ", x1, "x2: ", x2)
else:
    print("No hay solución")

if __name__ == "__main__":
    pass
