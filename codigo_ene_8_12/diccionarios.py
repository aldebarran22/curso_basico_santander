"""
Diccionarios en Python.
Creación, acceso a los elementos, recorridos ...
"""
d = {"nombre": "José", "edad": 34, "tno": 600993344}

print(d, type(d))
print(d["nombre"])
d["dni"] = "56000112G"  # Añade una nueva clave
d["edad"] = 44  # Modificar una clave
print(d)

# Recorrer un diccionario:
for clave, valor in d.items():
    print(clave, valor)

# Comprobar si existe una clave en el diccionario:
if "direccion" in d:
    print(d["direccion"])
else:
    print("no existe la dirección")

L = [100, 34, 45, 34, 200, 200, 67, 90, 45, 34, 200]
# Construir un histograma: 100:1, 34:3, 45:2 ...
d2 = dict()
for i in L:
    if i in d2:
        # El número ya existe, contamos uno mas.
        d2[i] += 1
    else:
        # La primera vez que vemos el número
        d2[i] = 1
