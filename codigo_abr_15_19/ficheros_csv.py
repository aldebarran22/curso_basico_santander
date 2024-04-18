"""
Leer un fichero CSV por líneas
"""


def leerFichero(path):
    """Leer un fichero CSV por linea y filtrar información"""
    fich = None
    try:
        fich = open(path, "r")
        for fila in fich:
            print(fila)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()


if __name__ == "__main__":
    leerFichero("../ficheros_curso/pedidos.csv")
