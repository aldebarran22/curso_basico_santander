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


def leerEscribirFichero(path, pais):
    f = None
    fout = None
    try:
        pathPais = f"../ficheros/{pais}.csv"
        f = open(path, "r")
        fout = open(pathPais, "w")
        for linea in f:
            # Limpiar el \n de cada linea:
            linea = linea.rstrip()
            if pais in linea:
                print(linea)
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
