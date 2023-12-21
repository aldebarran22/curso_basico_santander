"""
Ficheros. Entrada/Salida
"""
import sys


def testStdout(fichero=sys.stdout):
    productos = [
        {"id": 1, "producto": "portatil", "precio": 1200.567},
        {"id": 2, "producto": "HP", "precio": 2250.6},
        {"id": 3, "producto": "Impresora", "precio": 566.0},
    ]
    print("%-5s\t%-15s\t%8s" % tuple(productos[0].keys()), file=fichero)
    for d in productos:
        # print("%05d\t%-15s\t%8.2f" % (d["id"], d["producto"],  d["precio"]))
        print("%05d\t%-15s\t%8.2f" % tuple(d.values()), file=fichero)


def leerFichero(path):
    f = None
    try:
        f = open(path, "r")
        for linea in f:
            # Limpiar el \n de cada linea:
            linea = linea.rstrip()
            print(linea)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


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


if __name__ == "__main__":
    # leerFichero("../ficheros/Empleados.txt")
    leerEscribirFichero("../ficheros/Pedidos.txt", "Suiza")
    """
    f = open("productos.txt", "w")
    testStdout(f)
    f.close()
    """
