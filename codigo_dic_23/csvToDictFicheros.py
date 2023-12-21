"""
Implementar dos funciones:
csvToJson: Carga los datos de un fichero CSV.
jsonToCSV
"""


def csvToJson(fich, sep=";"):
    f = None
    try:
        f = open(fich, "r")
        csv = f.read()
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
    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if f:
            f.close()


def jsonToCSV(registros, sep=";"):
    cabs2 = sep.join(registros[0].keys())
    L2 = [cabs2]
    for reg in registros:
        fila = sep.join(reg.values())
        L2.append(fila)
    csv2 = "\n".join(L2)
    return csv2


if __name__ == "__main__":
    Ljson = csvToJson("../ficheros/Empleados.txt")    
    for d in Ljson:
        print(d)
    

    #csv = jsonToCSV(Ljson)
   
