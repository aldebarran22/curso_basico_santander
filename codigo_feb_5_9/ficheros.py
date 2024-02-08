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


def printFile():
    f = open("exportaciones/prueba.txt", "w")
    for i in range(5):
        print("mensaje de prueba", file=f)
    f.close()


if __name__ == "__main__":
    # printFile()
    leerFichero("../ficheros_curso/Pedidos.txt")
