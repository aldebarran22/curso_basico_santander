"""
Cargar una lista de diccionarios con un bloque
de texto en formato csv
"""

csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

# Partir el bloque de texto en lineas: \n
L = csv.split("\n")

# Colocar las cabeceras en una lista
cabs = L[0].split(';')
print(cabs)

# Iterar por el resto de filas creando los dicts
for fila in L[1:]:
    valores = fila.split(';')
    dicc = dict(zip(cabs, valores))
    print(dicc)


