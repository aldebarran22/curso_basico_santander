"""
Crear la conexión a la BD (comprobando si existe el fichero)
y lanzar consultas
"""
import sqlite3 as db
from os.path import isfile


def listarTabla(path, tabla):
    con = None
    cur = None
    try:
        if isfile(path):
            con = db.connect(path)
            cur = con.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs)
            for t in cur.fetchall():
                linea = ";".join([str(i) for i in t])
                print(linea)

        else:
            raise FileNotFoundError(f"El fichero {path} no existe...")

    except Exception as e:
        print(e.__class__.__name__, e)
        # raise e Relanzar una excepción
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    path = "../bd/empresa3.db"
    listarTabla(path, "empleados")
