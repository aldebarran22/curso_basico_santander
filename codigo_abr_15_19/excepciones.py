"""
Captura de errores en Python:
try, except, finally, raise
"""

from os import listdir

def prueba1():
    # Capturar una excepción
    try:
        L = [1, 4, 5, 6, 7]
        print(L[11])  # Falla y salta al except
        n = int("12f")  # Esta inst. no llega a ejecutarse!
        for i in L:
            print(i, end=" ")
        print()

    except IndexError as e:
        print("ERROR: ", e.__class__.__name__, e)


def prueba2():
    # Capturar dos posibles excepciones
    try:
        L = [1, 4, 5, 6, 7]
        print(L[1])
        n = int("12f")
        for i in L:
            print(i, end=" ")
        print()

    except IndexError as e:
        print("ERROR: ", e.__class__.__name__, e)

    except ValueError as e:
        print("ERROR: ", e.__class__.__name__, e)


def prueba3():
    # Capturar dos posibles excepciones agrupar en el
    # mismo tratamiento (except)
    # Y después capturar la excepción genérica.
    try:
        L = [1, 4, 5, 6, 7]
        print(L[1])
        n = int("12")
        print(n / 0)
        for i in L:
            print(i, end=" ")
        print()

    except (IndexError, ValueError) as e:
        print("ERROR: ", e.__class__.__name__, e)

    except Exception as e:
        print("ERROR: ", e.__class__.__name__, e)


def prueba4():
    # Apertura y cierre de un fichero con control de excepciones
    fich = None
    try:
        fich = open("../ficheros_curso/Alemania.txt", "r")
        txt = fich.read()
        #print(len(txt) / 0)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()

def procesarFich(path):
    ext = path.partition('.')[2]

    if ext == "txt":
        raise ValueError(f"Error en el fichero: {path}")
    else:
        print('procesando el fichero: ', path)

def prueba5():
    # Recorrer una carpeta de archivos, procesarlos y controlar los
    # ficheros que fallen en un proceso simulado:
    try:
        for f in listdir('../ficheros_curso'):
            procesarFich(f)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    # prueba4()
    prueba5()
