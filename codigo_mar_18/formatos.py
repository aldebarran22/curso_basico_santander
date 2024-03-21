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
    print(csv)


if __name__ == "__main__":
    formatearEnCols()
