"""
Capturar excepciones en Python
try, except, finally, raise
"""


def prueba1():
    """Capturar y tratar una excepción"""
    try:
        L = [1, 2, 3]
        print(L[10])
        print("mas código")
    except IndexError as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    prueba1()
