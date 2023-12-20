"""
Capturar y tratar excepciones en Python
"""


def test1():
    # Imprimir el mensaje de error
    try:
        L = [1, 2, 3, 4]
        print(L[10])
        print("mas código")
    except IndexError as e:
        print(e)


def test2():
    # Capturar 2 o más excepciones, con un tratamiento distinto
    # para cada excepción
    try:
        L = [1, 2, 3, 4]
        d = {"a":1, "b":2, "c":3}

        print(L[1])
        print("mas código")
        print(13 / 2)
        print(d["d"])

    except IndexError as e:
        print("IE", e)
    except ZeroDivisionError as e:
        print("Div 0: ", e)
    except Exception as e:
        print('Error general:', e.__class__.__name__, e)
    


if __name__ == "__main__":
    test2()
