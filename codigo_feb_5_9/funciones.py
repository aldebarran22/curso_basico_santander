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


if __name__ == "__main__":
    print("__name___ ", __name__)
    print(sumar2(12, 34))
    print(sumar2("12", "34"))
