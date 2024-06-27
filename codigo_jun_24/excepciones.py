"""
Capturar excepciones en Python:
try / except: monitorizar un grupo de instrucciones
finally: liberar recursos
raise: lanzar excepciones
"""

def test1():
    """Capturar una excepcion"""
    try:
        L = [1,2,3,4,5]
        print(L[10])
    except IndexError as e:
        print(e.__class__.__name__, e)


def test2():
    pass

if __name__ == "__main__":
    test1()
    # test2()