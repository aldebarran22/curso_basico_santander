"""
Fusionar dos ficheros de empleados en uno solo, quitando repetidos
"""

# definir una función que reciba el bloque de texto: CSV
# y devuelva un conjunto a nivel de filas.


def fusion(path1: str, path2: str, pathD: str, sep: str = "\n") -> str:

    def ordenar(fila):
        datos = fila.partition(";")
        if datos[0].isnumeric():
            return int(datos[0])
        else:
            return 0

    def csvToSet(path: str, sep: str = "\n") -> set:
        fich = None
        try:
            fich = open(path, "r")
            csv = fich.read()
            lineas = csv.split(sep)
            return set(lineas)
        except Exception as e:
            print(e)
        finally:
            if fich:
                fich.close()

    # Codigo de la funcion fusion
    c2 = csvToSet(path1)
    c3 = csvToSet(path2)
    todo = c2 | c3
    L = sorted(todo, key=ordenar)
    # print(todo)
    return sep.join(L)


if __name__ == "__main__":
    # Convertir el texto csv a un conjunto de filas:
    todo = fusion(
        "../ficheros_curso/Empleados2.txt",
        "../ficheros_curso/Empleados3.txt",
        "../ficheros/empleados_final.txt",
    )
    print(todo)
