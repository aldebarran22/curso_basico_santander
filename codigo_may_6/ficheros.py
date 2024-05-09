"""
Operaciones con ficheros: leer un fichero CSV por líneas,
exportar datos a ficheros con la función print
"""


def procesarCSV(path, sep=";"):
    fich = None
    try:
        paises = dict()
        fich = open(path, "r")
        for fila in fich:
            fila = fila.rstrip()
            L = fila.split(sep)
            pais = L[-1]
            importe = L[-2]
            print(pais, importe)

    except Exception as e:
        raise e
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    procesarCSV("../ficheros_curso/pedidos.csv")
