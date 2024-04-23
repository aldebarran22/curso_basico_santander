"""
Conjuntos en Python:
- Quitar repetidos
- Creación
- Añadir elementos
- Operadores: & | - ^
"""

c = {1, 1, 1, 2, 3, 1, 2, 6}
print(c, type(c))

L = [1, 2, 3, 4, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2, 7]
c2 = set(L)
print(c2)

L2 = list(set(L))
print(L2)


c2.add(12)
c2.add(77)
for i in c2:
    print(i, end=" ")
print()  # Salta de linea!


################################################################
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
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""
