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

cabs = "id;nombre;cargo"
val = "1;Davolio;Representante de ventas"
Lcabs = cabs.split(";")
Lval = val.split(";")
print(Lcabs)
print(Lval)


L = [1,2,3,4]
L2 = list("adios")
d2 = dict(zip(L, L2))
print(d2)


