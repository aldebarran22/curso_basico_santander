"""
Captura de excepciones en Python.
try, except, finally, raise
"""

from os import listdir


def test1():
    # Capturar una excepción concreta:
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["d"])  # lanza keyError
        print(L[10])  # IndexError
    except KeyError as e:
        print(e.__class__.__name__, e)


def test2():
    # Capturar una excepción pero salta otra excepción distinta:
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["a"])
        print(L[10])  # IndexError
    except KeyError as e:
        print(e.__class__.__name__, e)


def test3():
    # Capturamos a nivel de exception:
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["a"])
        print(L[10])  # IndexError
    except Exception as e:
        print(e.__class__.__name__, e)


def test4():
    # Capturamos una exception y luego capturamos posibles excepciones
    # de otro tipo
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["a"])
        print(L[10])  # IndexError

    except (KeyError, IndexError) as e:  # Excepciones particular
        print("error en el dict o en list: ", e)

    except Exception as e:  # Excepción más genérica
        print(e.__class__.__name__, e)


def test5(lanzar):
    if lanzar:
        raise ValueError("Se produce un error")

    else:
        print("todo bien")


def test6():
    fichero = None
    try:
        fichero = open("errores.py")
        fichero.read()
        return True

    except:
        print("error")

    finally:
        if fichero != None:
            fichero.close()


def procesar(fichero):
    n, _, ext = fichero.partition('.')
    if ext == 'png':
        raise ValueError(f"El fichero {fichero} no se puede procesar")
    else:
        print(f'Procesando el fichero {fichero}')

def test7():
    try:
        L = listdir()
        for f  in L:
            procesar(f)

    except  Exception as e:
        print(e)


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    """
    try:
        test5(True)
    except Exception as e:
        print(e)
    """
    #test6()
    test7()
