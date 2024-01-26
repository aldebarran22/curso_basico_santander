"""
Resolver una ecuacion de 2º grado con Python
ax^2 + bx + c = 0
x1 y x2
"""

import math


def ecuacion(a, b, c):
    raiz = b**2 - 4 * a * c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("No hay solución")


if __name__ == "__main__":
    resul = ecuacion(1, 5, 4)
    if resul:
        print(resul)
    else:
        print("No hay solución")
    resul = ecuacion(1, 2, 3)
    if resul:
        print(resul)
    else:
        print("No hay solución")
