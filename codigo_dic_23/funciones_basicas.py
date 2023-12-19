"""
Ejemplo de dos funciones en python. 
"""


def sumar(a, b):
    """Suma los valores a y b"""
    return a + b


def sumar3(a, b, c):
    """Suma los valores a, b y c"""
    return a + b + c


# Con tipos anotados:
def sumar2(a: str, b: str) -> str:
    return a + b


if __name__ == "__main__":
    print("El modulo: ", __name__, __doc__)
    print(sumar(1, 3), type(sumar), sumar.__name__, sumar.__doc__)
    print(sumar3(1, 3, 5))
    print(sumar2((1, 2), (3, 4)))
