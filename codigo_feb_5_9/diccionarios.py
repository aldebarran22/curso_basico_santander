"""
Diccionarios en Python.
Definir dicc
Acceso a los elementos
Bucles
"""

usuario = {"nombre": "Jorge", "edad": 34, "altura": 1.89}
print("El nombre:", usuario["nombre"])
# Incrementar la edad:
usuario["edad"] += 1
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
print(d["nombre"])
print("Todas las claves:")
for col, valor in d.items():
    print(col, valor)

L1 = "ana"  # Ojo la clave 'a' se machaca con el valor 3.
L2 = [1, 2, 3]
d = dict(zip(L1, L2))
d2 = dict(zip(L2, L1))
print(d)
print(d2)

# Histograma: 1:4, 2:4, 4:2
L = [1,2,2,2,1,1,1,2,4,5,5,6,7,6,4]
k = set(L) # Quitar repetidos.
print(k)
histo = dict()
for i in k:
    histo[i] = L.count(i)
print(histo)


