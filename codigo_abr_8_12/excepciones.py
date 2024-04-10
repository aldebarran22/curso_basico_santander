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

    L = os.listdir()
    errores = 0
    for f in L:
        try:
            procesar(f)
        except Exception as e:
            print(e)
            errores += 1

    if errores:
        print(f"Han fallado {errores} ficheros")


def test5():
    fich = None
    try:
        fich = open("ecuacion.py", "r")
        print(fich.read())

    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    test5()
