"""
Ficheros. Entrada/Salida
"""
import sys





def isFloat(numero):
    if type(numero) == str:
        if "." in numero:
            aux = numero.replace(".", "")
            return aux.isnumeric()
        else:
            return False
    else:
        return False


def replaceFloat(linea, sep=";"):
    # Partir la linea con split. Comprobar si una columna es un float
    # se cambia el . por la ,
    cols = linea.split(sep)
    L = [col.replace(".", ",") if isFloat(col) else col for col in cols]
    return sep.join(L)


def leerEscribirFichero(path, pais):
    f = None
    fout = None
    cabs = False
    try:
        pathPais = f"../ficheros/{pais}.csv"
        f = open(path, "r")
        fout = open(pathPais, "w")
        for linea in f:
            # Limpiar el \n de cada linea:
            linea = linea.rstrip()
            if not cabs:
                fout.write(linea + "\n")
                cabs = True

            if pais in linea:
                linea = replaceFloat(linea)
                fout.write(linea + "\n")
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
        if fout:
            fout.close()

