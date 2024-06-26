"""
Lectura/Escritura de ficheros en Python
"""

import sys

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
    fich = None
    try:
        fich = open(pathDestino, "w")
        c1 = cargaFichero(path1)
        c2 = cargaFichero(path2)

        fusion = c1 | c2
        L = sorted(fusion, key=criterio)
        L2 = [fila+"\n" for fila in L]
        fich.writelines(L2)

    except Exception as e:
        print(e)

    finally:
        if fich:fich.close()

def exportarPedidos(path, pais, sep=';', file=sys.stdout):
    fich = None
    try:
        fich = open(path, "r")
        for pos, fila in enumerate(fich):
            fila = fila.rstrip()
            if pos == 0:
                print(fila, file=file)
                continue

            L = fila.split(sep)
            if pais==L[-1]:
                print(fila, file=file)

    except Exception as e:
        print(e)
        
    finally:
        if fich:
            fich.close()

def exportarPais(path, *paises):
    for pais in paises:
        pathPais = f"../ficheros/{pais}.csv"
        fich = open(pathPais, "w")
        exportarPedidos(path, pais, file=fich)
        fich.close()


if __name__=='__main__':
    #grabarFichero("../ficheros/productos.txt")

    """
    fusionFicheros("../ficheros_curso/Empleados2.txt",
    "../ficheros_curso/Empleados3.txt",
    "../ficheros/empleados_fusion.txt")
    """

    exportarPedidos("../ficheros_curso/Pedidos.csv", "Finlandia")
    exportarPais("../ficheros_curso/Pedidos.csv","Finlandia", "Francia","Noruega")