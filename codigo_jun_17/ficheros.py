"""
Gestión de ficheros
"""

from os import listdir, remove

def leerFichero(path, sep=";"):
    fich = None
    try:
        # Borrar los ficheros de los países:
        for fichero in listdir("../ficheros/paises"):
            remove(f"../ficheros/paises/{fichero}")

        fich = open(path, "r")
        for fila in fich:
            fila = fila.rstrip()
            pais = fila.split(sep)[-1]
            pathPais = f"../ficheros/paises/{pais}.csv"
            fichPais = open(pathPais, "a")
            print(fila, file=fichPais)            
            fichPais.close()

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
