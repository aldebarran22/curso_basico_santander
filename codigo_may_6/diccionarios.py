"""
Diccionarios en Python
Pares de clave(inmutable)  - valor(lo que queramos)
Histogramas
Json
"""

d = {"1": 100, "2": 200, "3": 300}
print(d, type(d))

# Añadir nuevas claves:
d["4"] = 400
d["1"] = 1111
print(d)
print(d["2"])
# print(d["7"]) keyError una clave que no existe en el diccionario.

# Cargar un dicc con dos cadenas (con un sep)
claves = "id;nombre;cargo"
valores = "1;Davolio;Representante de ventas"
Lclaves = claves.split(";")
print(Lclaves)
Lvalores = valores.split(";")
print(Lvalores)
