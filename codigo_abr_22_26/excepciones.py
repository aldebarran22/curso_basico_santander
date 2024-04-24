"""
Capturar excepciones en Python
try, except, finally, raise
"""


def prueba1():
    """Capturar y tratar una excepción"""
    try:
        L = [1, 2, 3]
        print(L[1])
        print("mas código")
    except IndexError as e:
        print(e.__class__.__name__, e)


def prueba2():
    """Capturar y tratar varias excepciones"""
    try:
        L = [1, 2, 3]
        print(L[1] / 0)
        print("mas código")
    except IndexError as e:
        print(e.__class__.__name__, e)
    except ZeroDivisionError as e:
        print(e.__class__.__name__, e)


def prueba3():
    """Capturar y tratar dos excepciones
    particulares y otra más general"""
    try:
        L = [1, 2, 3]
        print(L[1] / 10)
        print(L[1] + "hola")
        print("mas código")
    except (ZeroDivisionError, IndexError) as e:
        print(e.__class__.__name__, e)
    except Exception as e:
        print(e.__class__.__name__, e)


def prueba4():
    """Abrir fichero y que lo deje cerrado
    si ha conseguido abrirlo"""
    f = None
    try:
        f = open("no_existe.txt", "r")
        txt = f.read()
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    prueba4()
