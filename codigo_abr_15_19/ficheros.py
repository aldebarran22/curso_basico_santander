"""
Gestión de ficheros en Python
"""

import sys


def leerFicheroEntero(path):
    """Cargar todo el contenido de un fichero, lo separa en filas
    y lo devuelve en un conjunto"""
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read().strip()
        L = txt.split("\n")
        return set(L)

    except Exception as e:
        # print(e.__class__.__name__, e)
        raise e

    finally:
        if fich != None:
            fich.close()


def criterio(linea):
    col = linea.partition(";")[0]
    if col.isnumeric():
        return int(col)
    else:
        return 0


def fusionFicheros(path1, path2, pathD):
    fich = None
    try:
        fich = open(pathD, "w")

        cemp2 = leerFicheroEntero(path1)
        cemp3 = leerFicheroEntero(path2)

        # Unión de conjuntos:
        empleados = cemp2 | cemp3

        # Ordenar:
        Lemp = sorted(empleados, key=criterio)

        # Imprimir el resultado:
        for e in Lemp:
            print(e, file=fich)

        print(f"Se ha generado correctamente el fichero: {pathD}")

    except Exception as e:
        print(e)

    finally:
        if fich != None:
            fich.close()


def grabarFicheroDePrueba():
    fich = open("../ficheros/pruebas.txt", "w")
    for i in range(10):
        print(f"LINEA {i+1} del fichero", file=fich)
    fich.close()


def grabarFichero(path):
    L = [
        {"producto": "portatil", "importe": 450.9},
        {"producto": "hp", "importe": 1450.69},
        {"producto": "teclado", "importe": 45.0},
    ]
    fich = None
    cabs = L[0].keys()
    try:
        fich = open(path, "w")
        print("%-12s\t%10s" % tuple(cabs), file=fich)
        for d in L:
            print("%-12s\t%10.2f" % tuple(d.values()), file=fich)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":

    if len(sys.argv) == 4:
        fusionFicheros(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        fusionFicheros(
            "../ficheros_curso/Empleados2.txt",
            "../ficheros_curso/Empleados3.txt",
            "../ficheros/Empleados_TODO.txt",
        )

    # grabarFicheroDePrueba()
    grabarFichero("../ficheros/productos.txt")
