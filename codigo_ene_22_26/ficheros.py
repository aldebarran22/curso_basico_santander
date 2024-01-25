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


def exportar(path, pais, sep=";"):
    fich = None
    fich2 = None
    importe = 0
    try:
        Lpath = path.split("/")
        pathPais = "/".join(Lpath[:-1]) + "/" + pais + ".txt"
        fich = open(path, "r")
        fich2 = open(pathPais, "w")
        for linea in fich.readlines():
            linea = linea.rstrip()
            L = linea.split(sep)
            if L[-1] == pais:
                fich2.write(linea + "\n")

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()
        if fich2:
            fich2.close()


def exportarPaises(path, *pais, sep=";"):
    fich = None
    fich2 = None
    importe = 0
    try:
        paises = dict()
        for p in pais:
            paises[p] = list()

        fich = open(path, "r")
        for linea in fich.readlines():
            linea = linea.rstrip()
            L = linea.split(sep)
            if L[-1] in paises:
                paises[L[-1]].append((linea+"\n"))

        # Ha terminado el fichero y grabamos los pedidos de cada país
        for p, L in paises.items():
            Lpath = path.split("/")
            pathPais = "/".join(Lpath[:-1]) + "/" + p + ".txt"
            fich2 = open(pathPais, "w")
            fich2.writelines(L)
            fich2.close()

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    # leerFichero('../ficheros/Pedidos.txt')

    # importe = sumaImporte("../ficheros/Pedidos.txt", "Suiza")
    # print("Importe: ", round(importe, 2))

    # exportar("../ficheros/Pedidos.txt", "Suiza")

    exportarPaises("../ficheros/Pedidos.txt", "Suiza", "Alemania", "Francia")
