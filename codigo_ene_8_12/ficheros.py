"""
Leer y escribir ficheros CSV con Python
"""


def leerFichero(path):
    """
    Imprimir el contenido en consola
    """
    fich = None
    try:
        # Abrir el fichero en modo lectura
        fich = open(path, "r")
        for linea in fich:
            # Limpia el carácter fin de línea (EOL)
            linea = linea.strip()
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich != None:
            fich.close()


def filtroPaises(path, *paises):
    """
    Imprimir el contenido en consola
    """
    fich = None
    try:
        # Abrir el fichero en modo lectura
        fich = open(path, "r")
        for linea in fich:
            # Limpia el carácter fin de línea (EOL)
            linea = linea.strip()
            columnas = linea.split(";")
            if columnas[-1] in paises:
                print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich != None:
            fich.close()


if __name__ == "__main__":
    # leerFichero("../ficheros/Pedidos.txt")
    filtroPaises("../ficheros/Pedidos.txt", "Suiza")
