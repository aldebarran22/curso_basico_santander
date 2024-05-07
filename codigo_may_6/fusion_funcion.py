"""
Fusionar dos ficheros de empleados en uno solo, quitando repetidos
"""

csv2 = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""

csv3 = """id;nombre;cargo
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Gerente de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""


# definir una función que reciba el bloque de texto: CSV
# y devuelva un conjunto a nivel de filas.


def fusion():

    def csvToSet(csv: str, sep: str = "\n") -> set:
        lineas = csv.split(sep)
        return set(lineas)

    # Codigo de la funcion fusion
    c2 = csvToSet(csv2)
    c3 = csvToSet(csv3)
    todo = c2 | c3
    return todo


if __name__ == "__main__":
    # Convertir el texto csv a un conjunto de filas:
    todo = fusion()
    for fila in todo:
        print(fila)
