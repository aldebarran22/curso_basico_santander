"""
Operaciones con ficheros: leer un fichero CSV por líneas,
exportar datos a ficheros con la función print
"""


def procesarCSV(path, sep=";"):
    fich = None
    cabs = True    
    try:
        paises = dict()
        fich = open(path, "r")
        for fila in fich:
            if cabs:
                cabs = False
                continue
            
            fila = fila.rstrip()
            L = fila.split(sep)
            pais = L[-1]
            importe = float(L[-2].replace(",","."))
            print(pais, importe)

    except Exception as e:
        raise e
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    procesarCSV("../ficheros_curso/pedidos.csv")
