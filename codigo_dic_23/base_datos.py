"""
Conexión a la BD sqlite3 con Python
"""
import sqlite3 as dbapi
from os.path import isfile


def test(path, tabla, pathFile):
    conexion = None
    cur = None
    fich = None
    try:
        if isfile(path):
            conexion = dbapi.connect(path)
            print("Conexión ok!")
            fich = open(pathFile, "w")
            cur = conexion.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs, file=fich)
            for t in cur.fetchall():
                linea = ";".join([str(i) for i in t])
                print(linea, file=fich)
        else:
            raise FileNotFoundError(f"El fichero {path} no existe")
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()
        if cur:
            cur.close()
        if conexion:
            conexion.close()


if __name__ == "__main__":
    test("../bd/empresa3.db", "categorias", "../ficheros/categorias.csv")
