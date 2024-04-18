"""
Gestión de ficheros en Python
"""


def leerFicheroEntero(path):
    """Devuelve todo el contenido de un fichero"""
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        return txt

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()

def criterio(linea):
    col = linea.partition(";")[0]
    if col.isnumeric():
        return int(col)
    else:
        return 0

def fusionFicheros(path1, path2):
    emp2 = leerFicheroEntero(path1)
    emp3 = leerFicheroEntero(path2)
    # Partir el contenido de emp2 en filas:
    Lemp2 = emp2.split("\n")

    # Partir el contenido de emp3 en filas:
    Lemp3 = emp3.split("\n")
    print(Lemp3[:3])

    # Convertir las dos listas en conjuntos
    cemp2 = set(Lemp2)
    cemp3 = set(Lemp3)

    # Unión de conjuntos:
    empleados = cemp2 | cemp3

    # Ordenar:
    Lemp = sorted(empleados, key=criterio)

    # Imprimir el resultado:
    for e in Lemp:
        print(e)

if __name__ == "__main__":
    fusionFicheros(
        "../ficheros_curso/Empleados2.txt", "../ficheros_curso/Empleados3.txt"
    )
