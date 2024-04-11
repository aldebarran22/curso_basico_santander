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
        print("%s\t%s" % tuple(cabs), file=fich)
        for d  in L:
            print("%s\t%f" % tuple(d.values()) ,file=fich)
        
    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()


if __name__=='__main__':
    grabarFichero("../ficheros/productos.txt")