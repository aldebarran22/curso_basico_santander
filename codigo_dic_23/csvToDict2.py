"""
Implementar dos funciones:
csvToJson
jsonToCSV
"""

texto = """idpedido;cliente;idempleado;idempresa;importe;pais
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


def csvToJson(csv, sep=";"):
    # Partir el bloque de texto en lineas: \n
    L = csv.split("\n")
    # Colocar las cabeceras en una lista
    cabs = L[0].split(sep)
    # Iterar por el resto de filas creando los dicts
    registros = []
    for fila in L[1:]:
        valores = fila.split(sep)
        dicc = dict(zip(cabs, valores))
        registros.append(dicc)

    return registros


def jsonToCSV(registros, sep=";"):
    cabs2 = sep.join(registros[0].keys())
    L2 = [cabs2]
    for reg in registros:
        fila = sep.join(reg.values())
        L2.append(fila)
    csv2 = "\n".join(L2)
    return csv2


if __name__ == "__main__":
    Ljson = csvToJson(texto)
    print(Ljson[:2])  # imprimir los dos primeros
    csv = jsonToCSV(Ljson)
    print(csv == texto)
