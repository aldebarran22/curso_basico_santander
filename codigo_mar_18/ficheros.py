"""
Leer y escribir ficheros
"""

from formatos import isfloat


def extraerPaises(path):
    """Leer el fichero de pedidos y devolver una colección con los paises"""
    fich = None
    paises = set()
    try:
        fich = open(path, "r")
        for pos, linea in enumerate(fich):
            linea = linea.rstrip()
            if linea == "" or pos == 0:
                continue

            L = linea.split(";")
            paises.add(L[-1])

        return sorted(paises)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def imprimirFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def acumuladoPaises(path, paises):
    dict_paises = dict.fromkeys(paises, 0)
    fich = None
    try:
        fich = open(path, "r")
        for pos, linea in enumerate(fich):
            linea = linea.rstrip()
            if linea == "" or pos == 0:
                continue

            L = linea.split(";")
            pais = L[-1]
            importe = float(L[-2]) if isfloat(L[-2]) else 0

            # Actualizar diccionario:
            dict_paises[pais] += importe

        return dict_paises

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def grabarFichero(path):
    fich = open(path, "w")
    for i in range(10):
        fich.write(f"linea de pedido {i+1}\n")

    L = [f"hola{i}\n" for i in range(20)]
    fich.writelines(L)
    fich.close()


if __name__ == "__main__":
    # imprimirFichero("../ficheros_curso/Pedidos.csv")
    paises = extraerPaises("../ficheros_curso/Pedidos.csv")
    # print(paises)
    histo = acumuladoPaises("../ficheros_curso/Pedidos.csv", paises)
    L = sorted(histo.items(), key=lambda t: t[1], reverse=True)
    for pais, importe in L:
        print(pais, round(importe, 2))

    grabarFichero("../ficheros/lineas.txt")
