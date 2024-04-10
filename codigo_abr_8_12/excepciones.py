"""
Control de excepciones en python
"""

import os


def test1():
    try:
        L = [1, 2, 3, 4, 5]
        print(L[30])
        print("fin")
    except IndexError as e:
        print(e.__class__.__name__, e)


def test2():
    try:
        L = [1, 2, 3, 4, 5]
        d = {"a": 1, "b": 2, "c": 3}
        print(d["a"])
        print(L[30])
        print("fin")
    except (IndexError, KeyError) as e:
        print(e.__class__.__name__, e)


def test3():
    try:
        L = [1, 2, 3, 4, 5]
        d = {"a": 1, "b": 2, "c": 3}
        print(d["a"])
        print(L[3])
        num = int("hola")

    except (IndexError, KeyError) as e:
        print(e.__class__.__name__, e)

    except Exception as e:
        print(e.__class__.__name__, e)


def test4():

    def procesar(f):
        if f.partition(".")[2] == "ipynb":
            raise ValueError(f"Error en el fichero: {f}")
        else:
            print(f"Procesando el fichero: {f}")

    try:
        L = os.listdir()
        for f in L:
            procesar(f)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test4()
