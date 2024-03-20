"""
Capturar excepciones en Python:
try, except, finally, raise
"""

from os import listdir


def test1():
    # Capturar 2 excepciones distintas
    try:
        L = [1, 2, 3, 4, 5]
        print(numero)
        print(L[10])
        print("mas codigo")

    except IndexError as e:
        print(e.__class__.__name__, e)

    except NameError as e:
        print(e.__class__.__name__, e)


def test2():
    # Capturar 2 excepciones distintas en una tupla (agrupar excepciones)
    # y otras excepciones de otros tipos
    try:
        L = [1, 2, 3, 4, 5]
        print(L[-1] / 0)
        print(numero)
        print(L[10])
        print("mas codigo")

    except (IndexError, NameError) as e:
        print(e.__class__.__name__, e)

    except Exception as e:
        print("Otro error: ", e)


def test3():
    # procesar ficheros dentro de un try except

    def procesarFichero(f):
        nombre, _, ext = f.partition(".")
        if nombre == "":
            return

        if ext != "py":
            raise ValueError(f"Error en el fichero {f}")
        else:
            print(f"procesando fichero {f}")

    try:
        L = listdir()
        for f in L:
            procesarFichero(f)

    except Exception as e:
        print(e)


def test4():
    # procesar ficheros dentro de un try except (TODOS LOS QUE PUEDA)
    # solo avisa de los que fallan pero continua

    def procesarFichero(f):
        nombre, _, ext = f.partition(".")
        if nombre == "":
            return

        if ext != "py":
            raise ValueError(f"Error en el fichero {f}")
        else:
            print(f"procesando fichero {f}")

        L = listdir()
        for f in L:
            try:
                procesarFichero(f)

            except Exception as e:
                print(e)


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()
