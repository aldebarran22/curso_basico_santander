"""
Capturar excepciones en Python
try, except, finally, raise
"""

from os import listdir


def prueba1():
    """Capturar y tratar una excepción"""
    try:
        L = [1, 2, 3]
        print(L[1])
        print("mas código")
    except IndexError as e:
        print(e.__class__.__name__, e)


def prueba2():
    """Capturar y tratar varias excepciones"""
    try:
        L = [1, 2, 3]
        print(L[1] / 0)
        print("mas código")
    except IndexError as e:
        print(e.__class__.__name__, e)
    except ZeroDivisionError as e:
        print(e.__class__.__name__, e)


def prueba3():
    """Capturar y tratar dos excepciones
    particulares y otra más general"""
    try:
        L = [1, 2, 3]
        print(L[1] / 10)
        print(L[1] + "hola")
        print("mas código")
    except (ZeroDivisionError, IndexError) as e:
        print(e.__class__.__name__, e)
    except Exception as e:
        print(e.__class__.__name__, e)


def prueba4():
    """Abrir fichero y que lo deje cerrado
    si ha conseguido abrirlo"""
    f = None
    try:
        f = open("fecha_hora.py", "r")
        txt = f.read()
        raise ValueError("Error en un parámetro")
        print(txt)
    except Exception as e:
        print(e.__class__.__name__, e)
        raise e
    finally:
        if f:
            f.close()


def procesarFich(path):
    ext = path.partition(".")[2]

    if ext == "txt":
        raise ValueError(f"Error en el fichero: {path}")
    else:
        print("procesando el fichero: ", path)


def prueba5():
    # Recorrer una carpeta de archivos, procesarlos y controlar los
    # ficheros que fallen en un proceso simulado:
    numErrores = 0
    for f in listdir("../ficheros_curso"):
        try:
            procesarFich(f)
        except Exception as e:
            print(e)
            numErrores += 1

    if numErrores > 0:
        print(f"Se han encontrado {numErrores} ficheros con error!")


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    # prueba4()
    prueba5()
