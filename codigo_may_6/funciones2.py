"""
Pasar por parámetro una función y ejecutarla
"""


def sumar(a, b, c, d):
    return a + b + c + d


def restar(a, b):
    return a - b


def ejecutar(funcion, *args, **kwargs):
    print("Vamos a ejecutar: ", funcion.__name__)
    print(funcion(*args, **kwargs))


if __name__ == "__main__":
    ejecutar(restar, 23, 45)
    ejecutar(sumar, 1, 2, 3, 4)

    # L = [1, 2, 3, 4]
    # L(0) Error, intenta ejecutar una función pero es una lista
