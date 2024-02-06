"""
Funciones en Python:
- Tipos anotados
- Tipos de parámetros
- Formas de llamar a la función
"""


def sumar(a, b):
    """
    Devuelve la suma de a y b
    """
    return a + b


def sumar2(a: int, b: int) -> int:
    """
    Devuelve la suma de a y b
    """
    return a + b


print(sumar2(12, 34))
print(sumar2("12", "34"))
