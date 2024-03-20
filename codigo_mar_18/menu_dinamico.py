"""
Generar un menú a partir de las funciones
almacenadas en una lista
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def salir(*args):
    exit()




if __name__ == "__main__":
    L = [sumar, restar, salir]
    while True:
        op = menu(L)

