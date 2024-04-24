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


if __name__ == "__main__":
    # prueba1()
    prueba2()
