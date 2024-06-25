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
7;King;Gerente de ventas
9;Dodsworth;Representante de ventas"""

filas = txt.split("\n")
cabs = filas[0].split(";")
empleados = list()
for fila in filas[1:]:
    Lvalores = fila.split(";")
    emp = dict(zip(cabs, Lvalores))
    empleados.append(emp)

print(empleados)
print('el nombre del primer empleado: ', empleados[0]['nombre'])
print('el cargo del último empleado: ', empleados[-1]['cargo'])

# Imprimir el nombre de los empleados que se dedican a las ventas
for emp in empleados:
    if "ventas" in emp['cargo'].lower():
        print(emp['nombre'])

"""
for pos, i in enumerate(filas):
    print(pos, i)
"""
