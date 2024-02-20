"""
Implementación de funciones en Python
Llamadas a las funciones:
Paso de parámetros
Tipos anotados
"""


def sumar(a, b):
    """
    Sumar los dos parámetros
    """
    return a + b


def sumar3(a, b, c):
    """
    Sumar los tres parámetros
    """
    return a + b + c


if __name__ == "__main__":
    print(sumar(1, 2))
    print(sumar("1", "2"))
    print(sumar([1], [2]))
    print(__name__)
