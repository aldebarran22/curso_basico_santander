"""
Leer un fichero CSV por líneas
"""


def leerFichero(path, *paises):
    """Leer un fichero CSV por linea y filtrar información"""
    fich = None
    try:
        fich = open(path, "r", encoding="iso-8859-1")
        for fila in fich:
            fila = fila.rstrip()
            print(fila)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()


if __name__ == "__main__":
    leerFichero("../ficheros_curso/pedidos.csv", "Finlandia","Suiza")
