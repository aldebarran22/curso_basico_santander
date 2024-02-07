"""
Captura de excepciones en Python.
try, except, finally, raise
"""


def test1():
    # Capturar una excepción concreta:
    try:
        d = {"a": 1, "b": 2}
        L = [1, 2, 3, 4]
        print(d["d"])
        print(L[10])
    except KeyError as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    test1()
