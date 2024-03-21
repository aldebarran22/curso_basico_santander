"""
Leer y escribir ficheros
"""


def extraerPaises(path):
    """Leer el fichero de pedidos y devolver una colección con los paises"""
    fich = None
    paises = set()
    try:
        fich = open(path, "r")
        for pos, linea in enumerate(fich):
            linea = linea.rstrip()
            if linea == "" or pos == 0:
                continue

            L = linea.split(";")
            paises.add(L[-1])

        return sorted(paises)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


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
    # imprimirFichero("../ficheros_curso/Pedidos.csv")
    paises = extraerPaises("../ficheros_curso/Pedidos.csv")
    print(paises)
