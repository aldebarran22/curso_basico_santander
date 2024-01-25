"""
Procesar ficheros en Python: lectura y Escritura
"""


def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich.readlines():
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def sumaImporte(path, pais, sep=";"):
    fich = None
    importe = 0
    try:
        fich = open(path, "r")
        for linea in fich.readlines():
            linea = linea.rstrip()
            L = linea.split(sep)
            if L[-1] == pais:
                importe += float(L[-2])

        return importe

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    # leerFichero('../ficheros/Pedidos.txt')
    importe = sumaImporte("../ficheros/Pedidos.txt", "Suiza")
    print("Importe: ", importe)
