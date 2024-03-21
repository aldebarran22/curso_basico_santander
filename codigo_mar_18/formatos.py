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
    tab = " " * 3
    for pos, fila in enumerate(L[:5]):
        if fila == "" or pos == 0:
            if pos == 0:
                t = tuple(fila.split(";"))
                print(f"%-8s{tab}%s\t%s\t%s\t%s\t%s" % t)
            continue

        cols = fila.split(";")
        cols = tuple([convertirTipos(i) for i in cols])
        print(f"%-8d{tab}%s\t%d\t%d\t%f\t%s" % cols)


if __name__ == "__main__":
    formatearEnCols()
