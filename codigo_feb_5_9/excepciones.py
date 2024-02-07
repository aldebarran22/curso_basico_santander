"""
Captura de excepciones en Python.
try, except, finally, raise
"""


def test1():
    # Capturar una excepción concreta:
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["d"]) # lanza keyError
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


if __name__ == "__main__":
    # test1()
    test2()
