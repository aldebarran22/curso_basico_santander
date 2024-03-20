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


def menu(L):
    print("Menú principal")
    for pos, f in enumerate(L):
        print(pos + 1, f.__name__)
    op = int(input("Seleccionar op:"))
    return op


if __name__ == "__main__":
    L = [sumar, restar, salir]
    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        op = menu(L)
        print("resul", L[op - 1](a, b))
