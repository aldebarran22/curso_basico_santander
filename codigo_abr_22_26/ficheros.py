"""
Ficheros en Python.
Escribir con la función print
Lectura de ficheros con: read y readline
"""

def grabarFichero(path):
    f = open(path, "w")
    for i in range(10):
        print(f"Linea {i+1}", file=f)
    f.close()

def ficheroEnCols():
    L = [("HP", 1200.0), ("Portatil",577.8), ("Teclado",56.776)]
    print("%-15s\t%8s" % ("PRODUCTO","IMPORTE"))
    for t in L:
        print("%-15s\t%8.2f" % t)

def leerFichero(path):
    """Leer un fichero CSV por filas"""
    f = None
    try:
        f = open(path, "r")
        for fila in f:
            fila = fila.rstrip() # Objeto inmutable -> machacar la variable!
            print(fila, f.tell())
    except Exception as e:
        print(e)
    finally:
        if f:f.close()


def calcularTotalPedidos(path, *paises, sep=";"):
    """Leer un fichero CSV por filas"""
    f = None
    try:
        f = open(path, "r")

        # Inicializar el dict con las claves (paises)
        dict_paises = dict.fromkeys(paises, 0)

        for fila in f:
            fila = fila.rstrip() # Objeto inmutable -> machacar la variable!
            
            # Partir con split (utilizar el sep)
            cols = fila.split(sep)

            # El país es la última col, comprobar si está o no en paises
            pais = cols[-1]
            if pais in paises:
                # Si está, incrementar con el importe: utilizar antes float() para convertirlo
                importe = float(cols[-2].replace(",","."))

                # Actualizar la clave del dict:
                dict_paises[pais] += importe

        return dict_paises

    except Exception as e:
        print(e)
    finally:
        if f:f.close()


if __name__ == "__main__":
    # grabarFichero("../ficheros/prueba.txt")
    # ficheroEnCols()
    leerFichero("../ficheros_curso/pedidos.csv")
    #d = calcularTotalPedidos("../ficheros_curso/pedidos.csv", "Suiza","Francia", "Alemania")
    #print(d)