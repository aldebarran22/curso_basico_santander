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


if __name__ == "__main__":
    # prueba1()
    prueba2()
