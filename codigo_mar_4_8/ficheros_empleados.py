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

if __name__ == "__main__":
    c1 = cargaFichero("../ficheros_curso/Empleados2.txt")
    c2 = cargaFichero("../ficheros_curso/Empleados3.txt")

    filasComunes = c1 & c2
    print("Filas comunes:")
    for f in filasComunes:
        print(f)

    fusion = c1 | c2
    filas = sorted(fusion, key=criterio)
    print("\n\nFusión:")
    for f in filas:
        print(f)

    fich = open("../ficheros/empleados.csv","w")
    fich.writelines([fila+"\n" for fila in filas])
    fich.close()
