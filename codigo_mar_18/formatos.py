"""
Imprimir registros en columnas.
"""

path = "../ficheros_curso/Pedidos.csv"


def isfloat(cad):
    if '.' in cad:
        num = cad.replace(".","")
        return num.isnumeric()
    else:
        return False



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
        if fila == "" or pos==0:
            continue

        cols = fila.split(";")
        cols = [int(i) if i.isnumeric() else i for i in cols]
        cols[-2] = float(cols[-2])
        print(cols)


if __name__ == "__main__":
    formatearEnCols()
