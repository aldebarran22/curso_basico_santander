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


def prueba3():
    fich = None
    try:
        fich = open("conjuntos.py", "r")
        resul = 2 + "2"

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def prueba4(num):
    if 0 <= num <= 10:
        print("numero: ", num)
    else:
        raise ValueError(f"El número {num} no cumple el intervalo")


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    try:
        prueba4(1)
    except ValueError as e:
        print(e)

