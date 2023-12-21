"""
Capturar los parámetros de la línea de comandos
"""
import sys

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

if __name__ == "__main__":
    leerFichero(sys.argv[0])