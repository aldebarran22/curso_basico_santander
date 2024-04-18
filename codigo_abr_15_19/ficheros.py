"""
Gestión de ficheros en Python
"""


def leerFicheroEntero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        return txt

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()


if __name__ == "__main__":
    txt1 = leerFicheroEntero("../ficheros_curso/Empleados2.txt")
    print(txt1)
