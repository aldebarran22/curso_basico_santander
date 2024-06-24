"""
Diccionarios en Python:
- Crear diccionarios
- Añadir y modificar claves
"""

d = {"a": 100, "b": 200, "c": 300}
d["d"] = 4  # Añadir una nueva clave.
d["a"] = 1  # Modificar una clave
# del(d["b"])
print(d, type(d))
print(d["a"] + d["b"])

# Pruebas con la función dict y zip
L = [1, 2, 3, 4, 5]
cad = "adios"
d2 = dict(zip(L, cad))
print(d2)

d3 = dict(zip(cad, L))
print(d3)

# Cuidado con los repetidos en las claves:
L = [1, 2, 2, 4, 4]
cad = "adios"
d2 = dict(zip(L, cad))
print(d2)
