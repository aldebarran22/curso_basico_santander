"""
- crear diccionarios
- dict / zip
- bucles
- añadir claves
- excepciones
"""

d = {"a":1, "b":2, "c":3}
print(d, type(d))

L = [1,2,3]
cad = "ABCDE"
d2 = dict(zip(cad, L))
print(d2)
d3 = dict(zip(L, cad))
print(d3)

cabs = "id;nombre;cargo"
val = "1;Davolio;Representante de ventas"
Lcabs = cabs.split(";")
Lval = val.split(";")
print(Lcabs)
print(Lval)
emp = dict(zip(Lcabs, Lval))
print(emp)