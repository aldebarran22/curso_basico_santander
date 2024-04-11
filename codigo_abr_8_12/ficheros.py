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
        L = [fila for fila in txt.split("\n") if len(fila) > 1]
        filas = set(L)
        return filas

    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()

def criterio(fila):
    valor = fila.partition(";")[0]
    if valor.isnumeric():
        return int(valor)
    else:
        return 0

def fusionFicheros(path1, path2, pathDestino):
    try:
        c1 = cargaFichero(path1)
        c2 = cargaFichero(path2)

        fusion = c1 | c2
        L = sorted(fusion, key=criterio)
        print(L)

    except Exception as e:
        print(e)


if __name__=='__main__':
    #grabarFichero("../ficheros/productos.txt")
    fusionFicheros("../ficheros_curso/Empleados2.txt",
    "../ficheros_curso/Empleados3.txt",
    "../ficheros/empleados_fusion.txt")