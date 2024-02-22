"""
Operaciones con ficheros en Python
"""
def leerFichero(path):
    f = None
    try:
        f = open(path, "r")
        for linea in f:
            linea = linea.rstrip()
            print(linea)        

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()

if __name__ == "__main__":
    leerFichero("../ficheros_curso/Pedidos.txt")