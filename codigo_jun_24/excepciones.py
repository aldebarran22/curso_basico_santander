"""
Capturar excepciones en Python:
try / except: monitorizar un grupo de instrucciones
finally: liberar recursos
raise: lanzar excepciones
"""

from os import listdir


def test1():
    """Capturar una excepcion"""
    try:
        L = [1, 2, 3, 4, 5]
        print(L[10])
        print("La suma es:", sum(L))

    except IndexError as e:
        print(e.__class__.__name__, e)


def test2():
    """Capturamos una excepcion, pero falla otra"""
    try:
        L = [1, 2, 3, 4, 5]
        n = 0
        print("La media: ", sum(L) / n)
        print(L[10])
        print("La suma es:", sum(L))

    except IndexError as e:
        print(e.__class__.__name__, e)


def test3():
    """Capturar dos excepciones. Puede haber dos
    except distinto o se pueden agrupar en el mismo
    except en una tupla"""
    try:
        L = [1, 2, 3, 4, 5]
        n = 0
        print("La media: ", sum(L) / n)
        print(L[10])
        print("La suma es:", sum(L))

    except (IndexError, ZeroDivisionError) as e:
        print(e.__class__.__name__, e)


def test4():
    """Capturar dos excepciones. Puede haber dos
    except distinto o se pueden agrupar en el mismo
    except en una tupla"""
    try:
        L = [1, 2, 3, 4, 5]
        n = 0
        print("La media: ", sum(L) / n)
        print(L[10])
        print("La suma es:", sum(L))

    except (IndexError, ZeroDivisionError) as e:
        if isinstance(e, IndexError):
            print("Es un indexerror")
        else:
            print(e.__class__.__name__, e)


def test5():
    """Capturar dos excepciones concretas. Y después
    capturamos con la superclase exception por si
    falla otra cosa."""
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4, 5]
        n = 0
        print(d["h"])
        print("La media: ", sum(L) / n)
        print(L[10])
        print("La suma es:", sum(L))

    except (IndexError, ZeroDivisionError) as e:
        print(e.__class__.__name__, e)

    except Exception as e:
        print(e.__class__.__name__, e)


def test6(path):
    """Capturar una excepción al abrir un fichero
    y liberar recursos (cerrar fichero) en
    finally"""
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        print(txt / 2)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich:
            fich.close()


def procesarFichero(path):
    if "cajero" in path:
        raise Exception(f"Error en el fichero: {path}")
    else:
        print(f"procesando el fichero: {path}")


def test7():
    try:
        for f in listdir():
            procesarFichero(f)

    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6("cadenas.py")
    test7()
