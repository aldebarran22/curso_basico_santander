"""
Capturar excepciones en Python:
try / except / finally / raise
"""


def test1():
    # Capturar una excepción
    try:
        L = [1, 2, 3, 4, 5]
        print(L[10])
        print(L[0] * 2)

    except IndexError as e:
        print(e)


def test2():
    # Capturar dos excepciones
    try:
        L = [1, 2, 3, 4, 5]
        print(L[1])
        print(L[0] / 0)

    except (ZeroDivisionError, IndexError) as e:
        print(e.__class__.__name__, e)


def test3():
    # Capturar dos excepciones y una más genérica
    try:
        L = [1, 2, 3, 4, 5]
        print(L[1])
        print(L[0] / 2)
        print(2 + "2")

    except (ZeroDivisionError, IndexError) as e:
        print(e.__class__.__name__, e)

    except Exception as e:
        print(e.__class__.__name__, e)


def test4():
    # Capturar excepciones con un fichero y dejarlo cerrado en finally
    f = None
    try:
        f = open("fecha_hora.py", "r", encoding="utf-8")
        txt = f.read()
        print(txt)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if f:
            f.close()


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()
