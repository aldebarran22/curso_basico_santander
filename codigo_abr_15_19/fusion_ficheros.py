"""
Fusionar dos ficheros de empleados en uno.
Quitando las filas repetidas
"""

emp2 = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""


emp3 = """id;nombre;cargo
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Gerente de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
5;Buchanan;Gerente de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""


def criterio(linea):
    col = linea.partition(";")[0]
    if col.isnumeric():
        return int(col)
    else:
        return 0


# Partir el contenido de emp2 en filas:
Lemp2 = emp2.split("\n")

# Partir el contenido de emp3 en filas:
Lemp3 = emp3.split("\n")
print(Lemp3[:3])

# Convertir las dos listas en conjuntos
cemp2 = set(Lemp2)
cemp3 = set(Lemp3)

# Unión de conjuntos:
empleados = cemp2 | cemp3

# Ordenar:
Lemp = sorted(empleados, key=criterio)

# Imprimir el resultado:
for e in Lemp:
    print(e)
