"""
Lectura/Escritura de ficheros en Python
"""

def grabarFichero(path):
    L = [{"producto":"portatil","importe":450.9},
    {"producto":"hp","importe":1450.69},
    {"producto":"teclado","importe":45.0}]
    fich = None
    cabs = L[0].keys()
    try:
        fich = open(path, "w")
        print("%-12s\t%10s" % tuple(cabs), file=fich)
        for d  in L:
            print("%-12s\t%10.2f" % tuple(d.values()) ,file=fich)
        
    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()

def cargaFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        filas = set(txt.split("\n"))
        return filas

    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()

def fusionFicheros(path1, path2, pathDestino):
    pass


if __name__=='__main__':
    grabarFichero("../ficheros/productos.txt")