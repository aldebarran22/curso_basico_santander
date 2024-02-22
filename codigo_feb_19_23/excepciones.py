"""
Captura de excepciones en Python
try except finally
raise
"""

from os import listdir


def prueba1():
    try:
        b = 10
        L = [1, 2, 3, 4]
        print(L[1])
        print(L[0] / b)
    except Exception as e:
        print(e.__class__.__name__, e)


def procesarFich(path):
    ext = path.partition(".")[2]
    if ext == "ipynb":
        raise ValueError(f"Error al procesar el fichero: {path}")
    else:
        print(f"Se ha procesado el fichero: {path}")


def prueba2():
    fallos = []
    for f in listdir():
        try:
            procesarFich(f)
            # raise IndexError('error en un index')

        except ValueError as e:
            fallos.append(f)

        except Exception as e:
            print(e.__class__.__name__, e)

    print(f"Han fallado {len(fallos)} ficheros")
    if len(fallos) > 0:
        print(fallos)


def prueba3():
    # Funcionamiento de finally
    L = []
    try:
        print("Va todo bien")
        print(L[2])
        return True
    except Exception as e:
        print(e)
    finally:
        print("Se ejecuta finally")


def pruebaFich(path):
    f = None
    try:
        f = open(path, "r")
        txt = f.read()
        print(txt)

    except Exception as e:
        raise e

    finally:
        if f:
            f.close()


if __name__ == "__main__":
    # prueba1()
    # prueba2()
    # prueba3()
    try:
        pruebaFich("noexiste.py")
    except Exception as e:
        print(e)
