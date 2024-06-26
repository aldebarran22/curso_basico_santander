"""
Convertir formato CSV a Lista de diccionarios.
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

if __name__=='__main__':

    # Convertir CSV a Lista de diccionarios:
    L = csv.split("\n")
    R = list()
    cabs = L[0].split(";")
    for linea in L[1:]:
        datos = linea.split(";")
        d = dict(zip(cabs, datos))
        # print(d)
        R.append(d)
    print(R)


    # Buscar los empleados que tienen de cargo: Representante de ventas
    for d in R:
        # if 'Representante de ventas' in d.values():
        if d["cargo"] == "Representante de ventas":
            print(d)
    print()


    # Convertir la Lista de diccionarios a CSV:
    cabs = ";".join(R[0].keys())
    R2 = [cabs]
    for d in R:
        linea = ";".join(d.values())
        R2.append(linea)
    csv2 = "\n".join(R2)
    print(csv == csv2)
