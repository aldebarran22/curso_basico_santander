"""
Procesamiento de ficheros en Python:
- Por líneas
- Grabar ficheros con write / print
"""


def leerFichero(path):
    """Leer el fichero por filas"""
    fich = None
    try:
        fich = open(path, "r")
        for fila in fich:
            print(fila)

    except Exception as e:
        raise e

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    leerFichero("diccionarios.py")
