"""
Fusionar dos ficheros de empleados en uno solo, quitando repetidos
"""

# definir una función que reciba el bloque de texto: CSV
# y devuelva un conjunto a nivel de filas.


def fusion(sep: str = "\n") -> str:

    def ordenar(fila):
        datos = fila.partition(";")
        if datos[0].isnumeric():
            return int(datos[0])
        else:
            return 0

    def csvToSet(csv: str, sep: str = "\n") -> set:
        lineas = csv.split(sep)
        return set(lineas)

    # Codigo de la funcion fusion
    c2 = csvToSet(csv2)
    c3 = csvToSet(csv3)
    todo = c2 | c3
    L = sorted(todo, key=ordenar)
    # print(todo)
    return sep.join(L)


if __name__ == "__main__":
    # Convertir el texto csv a un conjunto de filas:
    todo = fusion("../ficheros_curso/Empleados2.txt",
                  "../ficheros_curso/Empleados3.txt",
                  "../ficheros/empleados_final.txt")
    print(todo)
