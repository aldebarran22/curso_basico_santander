"""
Procesar ficheros en Python: lectura y Escritura
"""

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich.readlines():
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if fich: fich.close()

if __name__ == "__main__":
    leerFichero('../ficheros/Pedidos.txt')

