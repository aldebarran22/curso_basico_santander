"""
Resolver una ecuación de 2º grado en Python
ax^2 + bx + c = 0
En una función de python
"""

import math


def ecuGrado2(a, b, c):
    raiz = b**2 - 4 * a * c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return x1, x2
    else:
        return None


if __name__ == "__main__":
    a = 1
    b = 5
    c = 4

    resul = ecuGrado2(a, b, c)
    if resul:
        print("Resul: ", resul)
    else:
        print("No hay solución")
