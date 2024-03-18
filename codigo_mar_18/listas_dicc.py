"""
Cargar un bloque de texto en CSV a una lista de diccionarios
"""

txt = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

L = txt.split("\n")
R = list()
cabs = L[0].split(";")
for i in L[1:]:
    fila = i.split(";")
    print(fila)