"""
Captura de errores en Python:
try, except, finally, raise
"""


def prueba1():
    # Capturar una excepción
    try:
        L = [1, 4, 5, 6, 7]
        print(L[11])  # Falla y salta al except
        n = int("12f")  # Esta inst. no llega a ejecutarse!
        for i in L:
            print(i, end=" ")
        print()

    except IndexError as e:
        print("ERROR: ", e.__class__.__name__, e)


def prueba2():
    # Capturar dos posibles excepciones
    try:
        L = [1, 4, 5, 6, 7]
        print(L[11])  # Falla y salta al except
        n = int("12f")  # Esta inst. no llega a ejecutarse!
        for i in L:
            print(i, end=" ")
        print()

    except IndexError as e:
        print("ERROR: ", e.__class__.__name__, e)

    except ValueError as e:
        print("ERROR: ", e.__class__.__name__, e)


if __name__ == "__main__":
    # prueba1()
    prueba2()
