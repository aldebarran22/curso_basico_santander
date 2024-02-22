"""
Operaciones con ficheros en Python
"""
def leerFichero(path):
    f = None
    try:
        f = open(path, "r")
        

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()