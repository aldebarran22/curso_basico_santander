def ordenar(fila):
    aux = fila.partition(";")[0]
    if aux.isnumeric():
        return int(aux)
    else:
        return -1


def ordenarNombre(fila):
    nombre = fila.split(";")[1]
    if nombre == "nombre":
        return "0"
    else:
        return nombre
    
def cargaFichero(path):
    """Leer el fichero y devuelve un conjunto con las filas"""
    fich = None
    try:
        fich = open(path, "r")
        txt = fich.read()
        c = set([fila for fila in txt.split("\n") if len(fila) > 0])  
        return c
         
    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    c2 = cargaFichero("../ficheros_curso/Empleados2.txt")
    c3 = cargaFichero("../ficheros_curso/Empleados3.txt")
    
    todo = c2 | c3
    L = [fila for fila in todo if "nombre" not in fila]
    R = sorted(L, key=ordenar)
    R.insert(0, "id;nombre;cargo")
    csv = "\n".join(R)
    print(csv)
