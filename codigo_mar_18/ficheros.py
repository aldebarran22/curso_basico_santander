"""
Leer y escribir ficheros
"""

def extraerPaises(path):
    """Leer el fichero de pedidos y devolver una colección con los paises"""
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if fich:

def imprimirFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    imprimirFichero("../ficheros_curso/Pedidos.csv")
