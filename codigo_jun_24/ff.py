import sys


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
        c = set([fila for fila in txt.split("\n") if len(fila.strip()) > 0])
        return c

    except Exception as e:
        raise e

    finally:
        if fich:
            fich.close()


def fusion(origen1, origen2, destino):
    fich = None
    try:
        c2 = cargaFichero(origen1)
        c3 = cargaFichero(origen2)
        fich = open(destino, "w")

        todo = c2 | c3
        # L = [fila for fila in todo if "nombre" not in fila]
        R = sorted(todo, key=ordenar)
        # R.insert(0, "id;nombre;cargo")
        csv = "\n".join(R)
        print(csv, file=fich)
        print(f"Se ha generado el fichero: {destino}")

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ff.py <<origen1>> <<origen2>> <<destino>>")

    else:
        fusion(sys.argv[1], sys.argv[2], sys.argv[3])
