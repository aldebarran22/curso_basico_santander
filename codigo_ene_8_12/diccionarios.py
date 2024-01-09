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
