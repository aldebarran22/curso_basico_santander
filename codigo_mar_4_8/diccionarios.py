"""
Diccionarios en Python:
{}, dict, zip
acceso a los elementos
crear nuevas claves
"""

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(d["a"])
d["e"] = 5
print(d, type(d))

L = [1, 2, 3, 4, 5]
cad = "adios"
d2 = dict(zip(L, cad))
print(d2)
d3 = dict(zip(cad, L))
print(d3)

# in, for
d = {"a": 1, "b": 2, "c": 3, "d": 4}
print("Existe la clave: c: ", "c" in d)
print("Existe el valor: 2: ", 2 in d.values())

print("keys:", d.keys())
print("values: ", d.values())
print("items: ", d.items())
for k, v in d.items():
    print(k, v)

cabs = "id;nombre;cargo"
valores = "1;Davolio;Representante de ventas"
Lcabs = cabs.split(";")
Lvalores = valores.split(";")
empleado = dict(zip(Lcabs, Lvalores))
print(empleado)
print('el nombre: ', empleado['nombre'])
empleado['telefono'] = 913452233 # Crea una nueva clave
empleado['id'] = 102             # modifica una clave existente
print(empleado)
