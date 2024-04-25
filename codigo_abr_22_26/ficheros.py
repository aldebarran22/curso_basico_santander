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

if __name__ == "__main__":
    grabarFichero("../ficheros/prueba.txt")