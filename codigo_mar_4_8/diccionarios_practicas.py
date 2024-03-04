"""
Cambio de formato de CSV a json
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
print('Cabeceras: ', L[0])
print('Segundo empleado: ', L[2])
cabs = L[0].split(';')
empleados = list()
for fila in L[1:]:
    Lfila = fila.split(';')
    d = dict(zip(cabs, Lfila))
    empleados += [d]
print(empleados)



