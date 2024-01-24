"""
Control de excepciones en Python
"""


def test1():
    # Capturar una excepción concreta
    try:
        L = [1, 3, 4, 5, 6]
        print(L[15])
        print("última línea")
    except IndexError as e:
        print(e)
    # print("fin")


def test2():
    # Capturar una excepción concreta pero falla otra excepción distinta
    try:
        L = [1, 3, 4, 5, 6]
        print(100 / 0)
        print(L[15])
        print("última línea")
    except IndexError as e:
        print(e)


def test3():
    # Solución al caso test2
    try:
        L = [1, 3, 4, 5, 6]
        print(100 / 10)
        print(L[15])
        print("última línea")
    except Exception as e:
        print(e.__class__.__name__, e)


def test4():
    #  Una captura y otra más general
    try:
        num = 100
        nombre = "hola"
        d = {"a": 1, "b": 2, "c": 3}
        print(d["d"])
        print(num + num + nombre)
        print("última línea")

    except (IndexError, KeyError) as e:
        print("Falla la clave : ", e)

    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()
