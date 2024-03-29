import sys


def leerFichero(path, pais, file=sys.stdout):
    fich = None
    try:
        cabs = True
        fich = open(path, "r")
        for line in fich:
            line = line.rstrip()
            if cabs:
                print(line, file=file)
                cabs = False
                continue

            L = line.split(";")
            if pais == L[-1]:
                print(line, file=file)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if fich:
            fich.close()


def exportar(path, pais):
    pathPais = f"../ficheros/{pais}.csv"
    fich = open(pathPais, "w")
    leerFichero(path, pais, file=fich)
    fich.close()


def grabarFichero(path):
    fich = open(path, "w")
    for i in range(10):
        print(f"linea de pedido {i+1}", file=fich)
    fich.close()


if __name__ == "__main__":
    # leerFichero(r"..\ficheros_curso\Pedidos.csv")
    # leerFichero("../ficheros_curso/Pedidos.csv", "Noruega")
    # grabarFichero("../ficheros/prueba.txt")
    exportar("../ficheros_curso/Pedidos.csv", "Francia")
