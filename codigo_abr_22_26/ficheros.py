"""
Ficheros en Python.
Escribir con la función print
Lectura de ficheros con: read y readline
"""

def grabarFichero(path):
    f = open(path, "w")
    for i in range(10):
        print(f"Linea {i+1}", file=f)
    f.close()

def ficheroEnCols():
    L = [("HP", 1200.0), ("Portatil",577.8), ("Teclado",56.776)]
    print("%-15s\t%8s" % ("PRODUCTO","IMPORTE"))
    for t in L:
        print("%-15s\t%8.2f" % t)

if __name__ == "__main__":
    #grabarFichero("../ficheros/prueba.txt")
    ficheroEnCols()