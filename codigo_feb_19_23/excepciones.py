"""
Captura de excepciones en Python
try except finally
raise
"""

def prueba1():
    try:
        b = 0
        L = [1,2,3,4]
        print(L[10])
        print(L[0] /b)
    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    prueba1()