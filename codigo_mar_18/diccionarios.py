"""
Crear diccionarios
Funciones para crear diccionarios
Acceso a elementos
Añadir claves
bucle for
histogramas
"""

d = {"a":1, "b":2, "c":3}
print(d, type(d))

# Acceso a los elementos con [] y para crear nuevas claves o modificar también
d["a"] = 500
d["d"] = 4
print(d)
# print(d['e']) # Error la clave NO existe.
print(list(d.items()))
for k,v in d.items():
    print(k,v)
