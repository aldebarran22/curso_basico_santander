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


if __name__=='__main__':
    test1()