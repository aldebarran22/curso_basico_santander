"""
Capturar excepciones en Python:
try, except, finally, raise
"""


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
    try:
        L = [1, 2, 3, 4, 5]
        print(numero)
        print(L[10])
        print("mas codigo")

    except (IndexError, NameError) as e:
        print(e.__class__.__name__, e)



if __name__ == "__main__":
    test1()
