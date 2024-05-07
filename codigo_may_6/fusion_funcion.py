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

# Convertir el texto csv a un conjunto de filas:
L2 = csv2.split("\n")
# print(L2)
c2 = set(L2)
# print(c2)

c3 = set(csv3.split("\n"))
todo = c2 | c3
for fila in todo:
    print(fila)
