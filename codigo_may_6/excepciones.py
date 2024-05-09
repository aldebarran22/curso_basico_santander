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

    except IndexError as e:
        print(e)


if __name__ == "__main__":
    # test1()
    test2()
