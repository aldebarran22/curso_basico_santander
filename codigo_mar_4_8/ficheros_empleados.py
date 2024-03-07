"""
Cargar en dos conjuntos de string los ficheros de
empleados: empleados2.txt y empleados3.txt
"""


def cargaFichero(path):
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        print(txt)
    except Exception as e:
        pass
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    c1 = cargaFichero("../ficheros_curso/Empleados2.txt")
    c2 = cargaFichero("../ficheros_curso/Empleados3.txt")
