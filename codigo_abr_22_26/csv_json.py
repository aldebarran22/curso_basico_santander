"""
Convertir un formato en CSV a json y luego al revés:
Lista de dict --> csv
"""

csv = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""

# De CSV a json
lineas = csv.split("\n")
cabs = lineas[0].split(";")
emp = []  # list()
for datos in lineas[1:]:
    Ldatos = datos.split(";")
    e = dict(zip(cabs, Ldatos))
    print(e)
    emp.append(e)  # emp += [e]
print(f"Tenemos {len(emp)} empleados.")


# De json a CSV
cabs = emp[0].keys()
cabeceras = ";".join(cabs)
resul = [cabeceras]
for e in emp:
    valores = ";".join(e.values())
    resul.append(valores)
csv2 = "\n".join(resul)
print(csv == csv2)
