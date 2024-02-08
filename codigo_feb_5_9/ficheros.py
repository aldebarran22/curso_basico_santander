"""
Tratamiento de ficheros en Python
Leer / escribir en fichero y redirigir la salida
estandar a un fichero
"""


def leerFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        for i in fich:
            i = i.rstrip()  # machacar la variable: OJO es INMUTABLE!!!
            print(i)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def filtroPais(path, *paises):
    fich = None
    try:
        fich = open(path, "r")
        for linea in fich:
            linea = linea.rstrip()  # machacar la variable: OJO es INMUTABLE!!!
            L = linea.split(";")
            pais = L[-1]
            if pais in paises:
                importe = float(L[-2])
                print("%-12s\t%6.2f" % (pais, importe))

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def printFile():
    f = open("exportaciones/prueba.txt", "w")
    for i in range(5):
        print("mensaje de prueba", file=f)
    f.close()


def compararFicheros(path1, path2):

    cabs = None

    def cargaFichero(path):
        fich = open(path, "r")
        txt = fich.read()
        fich.close()

        L = txt.split("\n")
        cabs = L[0]
        return set(L[1:])

    c1 = cargaFichero(path1)
    c2 = cargaFichero(path2)

    # Buscar lineas coincidentes:
    lineas = c1 & c2
    lineas1 = c1 - c2
    lineas2 = c2 - c1

    todo = sorted(
        lineas1 | lineas2 | lineas, key=lambda cad: int(cad.partition(";")[0])
    )
    todo.insert(0, cabs)
    for i in todo:
        print(i)


if __name__ == "__main__":
    # printFile()
    # leerFichero("../ficheros_curso/Pedidos.txt")
    # filtroPais("../ficheros_curso/Pedidos.txt", "Alemania")
    # filtroPais("../ficheros_curso/Pedidos.txt", "Venezuela", "Suiza", "Italia")
    compararFicheros("exportaciones/Empleados2.txt", "exportaciones/Empleados3.txt")
