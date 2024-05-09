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
            importe = float(L[-2].replace(",", "."))
            if pais in paises:
                # El país ya existe se actualiza el importe
                paises[pais] += importe
            else:
                # Es la primera vez que aparece el país
                paises[pais] = importe

        return sorted(paises.items(), key=lambda t: t[1], reverse=True)

    except Exception as e:
        raise e
    finally:
        if fich:
            fich.close()


def grabar(path, paises):
    fich = open(path, "w")
    for t in paises:
        print("%-15s\t%8.2f" % t, file=fich)
    fich.close()


if __name__ == "__main__":
    paises = procesarCSV("../ficheros_curso/pedidos.csv")
    grabar("../ficheros/prueba.txt", paises)
