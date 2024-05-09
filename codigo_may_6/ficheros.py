"""
Operaciones con ficheros: leer un fichero CSV por líneas,
exportar datos a ficheros con la función print
"""


def procesarCSV(path):
    fich = None
    try:
        fich = open(path, "r")
        for fila in fich:
            print(fila)

    except Exception as e:
        raise e
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    procesarCSV("../ficheros_curso/pedidos.csv")
