import sqlite3 as db
from os.path import isfile


def conexion(path, tabla):
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
            for t in cur.fetchall():
                print(t)

    except Exception as e:
        # raise e
        print(e.__class__.__name__, e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    conexion("../bd/empresa3.db","pedidos2")
