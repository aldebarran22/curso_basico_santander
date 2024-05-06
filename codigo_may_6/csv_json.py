"""
Convertir un bloque de texto CSV a dict
"""

csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

filas = csv.split("\n")

# Almacenar las cabeceras y separarlas:
cabs = filas[0].split(";")
empleados = []  # empleados = list()

# Recorrer las filas pero saltando las cabeceras:
for datos in filas[1:]:

    # Separar los datos de cada empleado a partir del ;
    Ldatos = datos.split(";")

    # Mezclar las cabs con los datos del empleado y generar un diccionario
    # por cada empleado
    emp = dict(zip(cabs, Ldatos))
    empleados.append(emp)

print(empleados)

# Recorrer diccionario, acceder a un campo
# histogramas
