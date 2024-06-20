"""
Utilizar conjuntos para fusionar dos ficheros CSV
"""

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        filas = set(txt.split("\n"))
        return filas

    except Exception as e:
        raise e

    finally:
        if fich: fich.close()


def ordenar(linea):
    L = linea.split(";")
    if L[0].isnumeric():
        numero = int(L[0])
        return numero
    else:
        return 0

def grabarFichero(path, csv):
    fich = None
    try:
        fich = open(path, "w")
        print(csv, file=fich)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()


#c2 = set(txt2.split("\n"))
#c3 = set(txt3.split("\n"))

try:
    c2 = leerFichero("../ficheros_curso/Empleados2.txt")
    c3 = leerFichero("../ficheros_curso/Empleados3.txt")

    todo = c2 | c3
    L = sorted(todo, key=ordenar)
    csv = "\n".join(L)
    csv = csv.strip() # limpiar filas en blanco al final o al principio pero no en medio.
    grabarFichero("../ficheros/empleados_final.csv", csv)
    print('fichero generado correctamente ...')

except Exception as e:
    print(e.__class__.__name__, e)