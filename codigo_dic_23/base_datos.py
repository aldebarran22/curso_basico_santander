"""
Conexión a la BD sqlite3 con Python
"""
import sqlite3 as dbapi
from os.path import isfile


def test(path, tabla):
    conexion = None
    cur = None
    try:
        if isfile(path):
            conexion = dbapi.connect(path)
            print("Conexión ok!")
            cur = conexion.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs)
            for t in cur.fetchall():
                linea = ";".join([str(i) for i in t])
                print(linea)
        else:
            raise FileNotFoundError(f"El fichero {path} no existe")
    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if conexion:
            conexion.close()


if __name__ == "__main__":
    test("../bd/empresa3.db", "categorias")
