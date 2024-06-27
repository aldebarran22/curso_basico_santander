"""
Procesamiento de ficheros en Python:
- Por líneas
- Grabar ficheros con write / print
"""


def grabarFichero(path):
    fich = None
    try:
        fich = open(path, "a")
        for i in range(10):
            # print(f"fila {i+1}", file=fich)
            fich.write(f"fila {i+1}")

    except Exception as e:
        raise e

    finally:
        if fich:
            fich.close()


def leerFichero(path, pais, sep=";"):
    """Leer el fichero por filas"""
    fich = None
    try:
        fich = open(path, "r")
        for fila in fich:
            fila = fila.strip()  # ojo es inmutable!
            L = fila.split(sep)
            if L[-1] == pais:
                print(fila)

    except Exception as e:
        raise e

    finally:
        if fich:
            fich.close()


def exportarPais(path, pais, sep=";"):
    """Grabar un fichero con las filas de los
    pedidos del pais indicado"""
    fich = None
    fichPais = None
    cabs = True
    try:
        path_destino = f"../ficheros/{pais}.csv"
        fich = open(path, "r")
        fichPais = open(path_destino, "w")
        print("filas: ", len(fich))

        for fila in fich:
            fila = fila.strip()  # ojo es inmutable!

            if cabs:
                print(fila, file=fichPais)
                cabs = False
                continue

            L = fila.split(sep)
            if L[-1] == pais:
                print(fila, file=fichPais)

    except Exception as e:
        raise e

    finally:
        if fichPais:
            fichPais.close()

        if fich:
            fich.close()


if __name__ == "__main__":
    # leerFichero("../ficheros_curso/pedidos.csv", "Suiza")
    grabarFichero("../ficheros/lineas.txt")
    # exportarPais("../ficheros_curso/pedidos.csv", "Suiza")
