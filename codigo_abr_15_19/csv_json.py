"""
Convertir formato CSV a Lista de dicts.
Y al revés también
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

# De CSV a lista de diccionarios:
L = csv.split("\n")
cabs = L[0].split(";")
empleados = []

for i in L[1:]:
    lval = i.split(";")
    emp = dict(zip(cabs, lval))
    #print(emp)
    empleados += [emp]

print(empleados[:3])

# Imprimir solo el nombre de los empleados:
for emp in empleados:
    print(emp['nombre'])
