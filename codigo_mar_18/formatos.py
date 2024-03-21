"""
Imprimir registros en columnas.
"""

path = "../ficheros_curso/Pedidos.csv"


def formatearEnCols():

    def leerFichero():
        fich = open(path, "r")
        txt = fich.read()
        fich.close()
        return txt

    # formatearEnCols:
    csv = leerFichero()
    # print(csv)

    # Partir en filas y cols:
    L = csv.split("\n")
    for fila in L:
        if fila == "":
            continue

        cols = fila.split(";")
        print(cols)


if __name__ == "__main__":
    formatearEnCols()
