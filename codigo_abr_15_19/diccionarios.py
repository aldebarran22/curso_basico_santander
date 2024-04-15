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
cad = "ABC"
d2 = dict(zip(cad, L))
print(d2)
d3 = dict(zip(L, cad))
print(d3)