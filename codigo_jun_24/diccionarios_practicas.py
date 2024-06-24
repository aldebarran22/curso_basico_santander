"""
Prácticas sobre diccionarios
"""

# {"id":"1", "nombre":"Davolio", "cargo":"Representante de ventas"}
cabs = "id;nombre;cargo"
valores = "1;Davolio;Representante de ventas"

Lcabs = cabs.split(";")
Lvalores = valores.split(";")
emp = dict(zip(Lcabs, Lvalores))
print(emp)
print(emp["nombre"])
