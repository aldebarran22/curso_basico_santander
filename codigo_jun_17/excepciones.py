"""
Capturar excepciones en Python:
- try, except: para capturar excepciones
 - finally: para liberar recursos
 - raise: lanzar excepciones
"""

from os import listdir

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

    except ValueError as e:
        print(e.__class__.__name__, e)


def test3():
    """Agrupar dos excepciones en el mismo except"""
    try:
        L = [1,2,3,4,5,6]
        numero = int("hola")
        print(L[10])
        print("continua")

    except (IndexError, ValueError) as e:
        print(e.__class__.__name__, e)
  
def test4():
    """Agrupar dos excepciones en el mismo except y capturar otras excepciones"""
    try:
        c = {1,2,3,4}
        L = [1,2,3,4,5,6]
        print(c[0])
        numero = int("hola")
        print(L[10])
        print("continua")

    except (IndexError, ValueError) as e:
        # Primero las excepciones más particulares
        print(e.__class__.__name__, e)

    except Exception as e:
        # Segundo el resto de excepciones con la super clase.
        #print(e.__class__.__name__, e)
        raise e

def test5():
    fich = None
    try:
        fich = open("decodadores.txt", "r")
        txt = fich.read()
        print(txt)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()


def procesarArchivo(path):
    ext = path.partition(".")[2]
    if ext == 'ipynb':
        raise ValueError(f"El fichero: {path} tiene un formato incorrecto")
    else:
        print(f"procesando fichero: {path}")

def test6():
    try:
        L = listdir()
        for f in L:
            procesarArchivo(f)
    except Exception as e:
        print(e)

if __name__=='__main__':
    #test1()
    #test2()
    #test3()
    """
    try:
        test4()
    except Exception as e:
        print(e.__class__.__name__, e)
    """
    test5()