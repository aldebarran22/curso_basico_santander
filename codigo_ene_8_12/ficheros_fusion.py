"""
A partir de dos ficheros de empleados, fusionar
los datos en otro fichero nuevo y dejarlos ordenados
por id. No añadir repetidos.
"""


def cargaFichero(path):
    """
    Leer el fichero entero, separar en linea
    y cargarlo a un conjunto.
    """
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        # Parte el texto por el salto de linea
        # y lo guarda en un conjunto
        c = set(txt.split("\n"))
        return c

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def ordenar(linea):
    t = linea.partition(";")
    if t[0].isnumeric():
        return int(t[0])
    else:
        return 0


def grabarFichero(path, L):
    """
    Grabar todas las líneas de la lista en un fichero.
    """
    fich = None
    try:
        fich = open(path, "w")
        fich.writelines(L)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    c1 = cargaFichero("Empleados2.txt")
    c2 = cargaFichero("Empleados3.txt")
    todo = c1 | c2
    L = sorted(todo, key=ordenar)
    # Añade un salto de línea al final de cada cadena:
    L = [linea + "\n" for linea in L]
    grabarFichero("Empleados_todo.txt", L)
