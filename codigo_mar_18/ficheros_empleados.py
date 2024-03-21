"""
Cargar en dos conjuntos de string los ficheros de
empleados: empleados2.txt y empleados3.txt
"""


def cargaFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        L = txt.split("\n")
        c = set([linea for linea in L if len(linea) > 1])
        return c

    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def criterio(fila):
    t = fila.partition(";")
    if t[0].isnumeric():
        return int(t[0])
    else:
        return 0


def fusion(pathO1, pathO2, pathDestino):
    c1 = cargaFichero(pathO1)
    c2 = cargaFichero(pathO2)

    fusion = c1 | c2
    filas = sorted(fusion, key=criterio)

    fich = open(pathDestino, "w")
    fich.writelines([fila + "\n" for fila in filas])
    fich.close()


if __name__ == "__main__":
    path1 = "../ficheros_curso/Empleados2.txt"
    path2 = "../ficheros_curso/Empleados3.txt"
    pathD = "../ficheros/empleados_final.csv"
    fusion(path1, path2, pathD)
