"""
Capturar excepciones en Python:
- try, except: para capturar excepciones
 - finally: para liberar recursos
 - raise: lanzar excepciones
"""

def test1():
    """Capturar una excepcion"""
    try:
        L = [1,2,3,4,5,6]
        print(L[10])
        print("continua")
    except IndexError as e:
        print(e.__class__.__name__, e)

def test2():
    """Capturar una excepcion, pero se produce otra distinta"""
    try:
        L = [1,2,3,4,5,6]
        numero = int("hola")
        print(L[10])
        print("continua")
    except IndexError as e:
        print(e.__class__.__name__, e)


if __name__=='__main__':
    #test1()
    test2()