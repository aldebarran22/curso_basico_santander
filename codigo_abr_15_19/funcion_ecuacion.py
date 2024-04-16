"""
Calcular ecuaciones de 2 grado en Python
ax^2 + bx + c = 0
"""

import math


def ecuacion(a, b, c):
    """Calcular la ecu. de 2 grado"""
    raiz = b**2 - 4 * a * c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return x1, x2
    else:
        return None


if __name__ == "__main__":
    # print("__name__:", __name__)

    # Inicialización múltiples:
    num1, num2, num3 = 1, 5, 4

    # llamada a la función:
    resul = ecuacion(num1, num2, num3)
    if resul:
        x1, x2 = resul
        print("Sol1: ", x1)
        print("Sol2: ", x2)
        # print("Solución: ", resul)
    else:
        print("No hay Solución")
