"""
Imprimir registros en columnas.
"""

path = "../ficheros_curso/Pedidos.csv"


def isfloat(cad):
    if "." in cad:
        num = cad.replace(".", "")
        return num.isnumeric()
    else:
        return False


def convertirTipos(valor):
    if valor.isnumeric():
        return int(valor)

    elif isfloat(valor):
        return float(valor)

    else:
        return valor


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
    for pos, fila in enumerate(L):
        if fila == "" or pos == 0:
            continue

        cols = fila.split(";")
        cols = tuple([convertirTipos(i) for i in cols])
        print("%d\t%s\t%d\t%d\t%f\t%s" % cols)


if __name__ == "__main__":
    formatearEnCols()
