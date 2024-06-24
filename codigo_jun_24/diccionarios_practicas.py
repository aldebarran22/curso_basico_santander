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

txt = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""

filas = txt.split("\n")
