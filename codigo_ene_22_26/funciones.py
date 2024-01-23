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


if __name__ == "__main__":
    print(math.sqrt(25))
    print(sqrt([1], [2], [3]))
    print(type(sqrt))
    print(sqrt.__name__, sqrt.__doc__)
    print(__name__, __doc__)

    f = sumar
    print(f, type(f))
    print(f(1, 2))

    L = [1, 2, 3]
    # print(L(0)) Error. Lo toma como si fuera una función y no lo es.
