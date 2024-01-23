"""
Funciones en python. Llamada, definición, documentación
Tipos anotados
"""

import math


def sumar(a, b):
    """
    Suma los dos parámetros recibidos
    """
    return a + b


def sqrt(a: int, b: int, c: int) -> int:
    """
    Suma los tres parámetros recibidos
    """
    return a + b + c


print(math.sqrt(25))
print(sqrt([1], [2], [3]))
print(type(sqrt))
print(sqrt.__name__, sqrt.__doc__)