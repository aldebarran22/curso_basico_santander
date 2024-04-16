"""
Calcular ecuaciones de 2 grado en Python
ax^2 + bx + c = 0
"""

import math


def ecuacion(a,b,c):
    raiz = b**2 - 4*a*c
    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2*a)
        x2 = (-b - math.sqrt(raiz)) / (2*a)
        return x1, x2
    else:
        return None


# Inicialización múltiples:
num1, num2, num3 = 1,5,4

# llamada a la función:
ecuacion(num1, num2, num3)

