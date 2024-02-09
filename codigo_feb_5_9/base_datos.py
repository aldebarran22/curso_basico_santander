import sqlite3 as db
from os.path import isfile
import sys

def conexion(path, tabla, file=sys.stdout):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"El fichero {path} no existe")
        else:
            con = db.connect(path)
            cur = con.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs, file=file)

            for t in cur.fetchall():
                linea = ";".join([str(i) for i in t])
                print(linea, file=file)

    except Exception as e:
        # raise e
        print(e.__class__.__name__, e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()

def exportar(path, tabla):
    pathFile = f"exportaciones/{tabla}.csv"
    f = open(pathFile, "w")
    conexion(path, tabla, f)
    f.close()

if __name__ == "__main__":
    exportar("../bd/empresa3.db","pedidos")
