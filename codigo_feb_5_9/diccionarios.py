"""
Diccionarios en Python.
Definir dicc
Acceso a los elementos
Bucles
"""
usuario = {"nombre":"Jorge", "edad":34, "altura":1.89}
print('El nombre:', usuario["nombre"])
# Incrementar la edad:
usuario["edad"]+=1
print(usuario, type(usuario))
usuario["peso"] = 78
print(usuario)

cabs = "id;nombre;cargo"
datos = "1;Davolio;Representante de ventas"
Lcabs = cabs.split(";")
Ldatos = datos.split(";")
print(Lcabs)
print(Ldatos)
d = dict(zip(Lcabs, Ldatos))
print(d)
print(d['nombre'])
print('Todas las claves:')
for col, valor in d.items():
    print(col, valor)