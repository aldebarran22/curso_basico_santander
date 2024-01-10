"""
Almacenar y ejecutar funciones que están en listas
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def mul(a, b):
    return a * b


def salir(*args):
    exit()


def menu(L):
    while True:
        a = int(input("Dame a:"))
        b = int(input("Dame b:"))

        # Pintar el menú en la consola:
        for pos, f in enumerate(L):
            print(pos + 1, f.__name__)
        op = int(input("Seleccionar opción:"))
        resul = L[op - 1](a, b)  # Ejecuta la función seleccionada
        print("Resultado: ", resul)


if __name__ == "__main__":
    L = [sumar, restar, mul, salir]
    menu(L)
    """
    print(L[0](1,2))

    i = sumar
    print(i(1,2))
    """
