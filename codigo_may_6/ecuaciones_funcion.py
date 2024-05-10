"""
Ecuaciones de segundo grado
"""

import math


def ecuacion(a, b, c):
    """Calculo de ecuaciones de 2 grado"""
    raiz = b**2 - 4 * a * c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return x1, x2
    else:
        raise ValueError("La ecuación no tiene solución")


if __name__ == "__main__":
    # Solo se ejecuta cuando ejecutamos el módulo
    print(ecuacion(1, 5, 4))
