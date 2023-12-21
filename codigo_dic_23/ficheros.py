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
    print("%-5s\t%-15s\t%8s" % tuple(productos[0].keys()),file=fichero)
    for d in productos:
        # print("%05d\t%-15s\t%8.2f" % (d["id"], d["producto"],  d["precio"]))
        print("%05d\t%-15s\t%8.2f" % tuple(d.values()),file=fichero)


if __name__ == "__main__":
    f = open("productos.txt","w")
    testStdout(f)
    f.close()
