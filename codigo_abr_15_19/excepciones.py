"""
Captura de errores en Python:
try, except, finally, raise
"""


def prueba1():
    # Capturar una excepción
    try:
        L = [1,4,5,6,7]
        print(L[10])
        for i in L:
            print(i, end=" ")
        print()

    except IndexError as e:
        print("ERROR: ", e)
        



if __name__ == "__main__":
    prueba1()
