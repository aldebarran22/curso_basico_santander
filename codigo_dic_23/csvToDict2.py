"""
Implementar dos funciones:
csvToJson
jsonToCSV
"""


def csvToJson():
    pass


def jsonToCSV():
    pass


csv = """idpedido;cliente;idempleado;idempresa;importe;pais
10248;WILMK;5;3;32.38;Finlandia
10249;TOMSP;6;1;11.61;Alemania
10250;HANAR;4;2;65.83;Brasil
10251;VICTE;3;1;41.34;Francia
10252;SUPRD;4;2;51.30;Belgica
10253;HANAR;3;2;58.17;Brasil
10254;CHOPS;5;2;22.98;Suiza
10255;RICSU;9;3;148.33;Suiza
10256;WELLI;3;2;13.97;Brasil
10257;HILAA;4;3;81.91;Venezuela
10258;ERNSH;1;1;140.51;Austria"""

# Partir el bloque de texto en lineas: \n
L = csv.split("\n")

# Colocar las cabeceras en una lista
cabs = L[0].split(";")

# Iterar por el resto de filas creando los dicts
registros = []
for fila in L[1:]:
    valores = fila.split(";")
    dicc = dict(zip(cabs, valores))
    registros.append(dicc)

print(registros)

print("-" * 10)

# Proceso invertido: lista de diccionarios -> texto en CSV
# Las claves del primer diccionario:
cabs2 = ";".join(registros[0].keys())
L2 = [cabs2]
for reg in registros:
    fila = ";".join(reg.values())
    L2.append(fila)
csv2 = "\n".join(L2)
print(csv2)
print(csv == csv2)
