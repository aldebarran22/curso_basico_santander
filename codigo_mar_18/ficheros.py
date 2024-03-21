"""
Leer y escribir ficheros
"""


def imprimirFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    imprimirFichero("../ficheros_curso/Pedidos.csv")
