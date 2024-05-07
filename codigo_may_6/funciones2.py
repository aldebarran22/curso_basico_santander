"""
Pasar por parámetro una función y ejecutarla
"""


def sumar(a, b, c, d):
    return a + b + c + d


def restar(a, b):
    return a - b


def ejecutar(funcion, *args, **kwargs):
    print(funcion(*args, **kwargs))


if __name__ == "__main__":
    ejecutar(restar, 23, 45)
    ejecutar(sumar, 1, 2, 3, 4)
