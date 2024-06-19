"""
Utilizar conjuntos para fusionar dos ficheros CSV
"""

txt2 = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""

txt3 = """id;nombre;cargo
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Gerente de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""


def ordenar(linea):
    L = linea.split(";")
    if L[0].isnumeric():
        numero = int(L[0])
        return numero
    else:
        return 0


c2 = set(txt2.split("\n"))
c3 = set(txt3.split("\n"))

todo = c2 | c3
L = sorted(todo, key=ordenar)
csv = "\n".join(L)
print(csv)
