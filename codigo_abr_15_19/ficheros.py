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
        txt = fich.read()
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


def fusionFicheros(path1, path2):
    try:
        cemp2 = leerFicheroEntero(path1)
        cemp3 = leerFicheroEntero(path2)

        # Unión de conjuntos:
        empleados = cemp2 | cemp3

        # Ordenar:
        Lemp = sorted(empleados, key=criterio)

        # Imprimir el resultado:
        for e in Lemp:
            print(e)

    except Exception as e:
        print(e)


def grabarFicheroDePrueba():
    fich = open("../ficheros/pruebas.txt","w")
    for i in range(10):
        print(f"Linea {i+1} del fichero", file=fich)
    fich.close()



if __name__ == "__main__":
    """
    fusionFicheros(
        "../ficheros_curso/Empleados2.txt", "../ficheros_curso/Empleados3.txt"
    )
    """
    grabarFicheroDePrueba()
