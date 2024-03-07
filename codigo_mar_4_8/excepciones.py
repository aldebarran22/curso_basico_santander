"""
Captura de errores.
try, except, finally, raise
"""


def prueba1():
    # Capturar una excepción concreta
    try:
        L = [1, 2, 3, 4]
        print(L[20])
        print("mas codigo")
    except IndexError as e:
        print(e)


def prueba2():
    # Capturar dos excepciónes concreta y otras de forma genérica
    try:
        L = [1, 2, 3, 4]
        d = {"a": 1, "b": 2}
        resul = 2 + "2"
        print(d["z"])
        print(L[20])
        print("mas codigo")
    except (IndexError, KeyError) as e:
        print(e)
    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # prueba1()
    prueba2()
