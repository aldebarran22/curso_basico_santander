"""
Capturar excepciones en Python:
try / except: monitorizar un grupo de instrucciones
finally: liberar recursos
raise: lanzar excepciones
"""


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
        print("La media: ", sum(L)/n)
        print(L[10])
        print("La suma es:", sum(L))

    except IndexError as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    #test1()
    test2()
