"""
Convertir un bloque de texto CSV a una lista 
de diccionarios
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
cabs = L[0].split(";")
R = []
for i in L[1:]:
    datos = i.split(";")
    d = dict(zip(cabs, datos))
    R.append(d)
print(R)

"""
s = ";".join(cabs)
print(cabs)
print(s)
"""
