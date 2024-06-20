"""
Gestión de ficheros
"""

def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for fila in fich:
            print(fila)            

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()
    

def grabarFichero(path):
    fich = None
    try:
        fich = open(path, "w")
        for i in range(10):
            print(f"linea: {i+1}", file=fich)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich: fich.close()
    


if __name__=='__main__':
    #grabarFichero("../ficheros/pruebas.txt")
    leerFichero("../ficheros_curso/Pedidos.csv")
