"""
Conectar con la BD sqlite3.
Crear conexiones y cursores. Ejecutar una consulta.
"""

import sqlite3 as dbapi
from os.path import isfile


def consulta(tabla, path, sep=";"):
    """
    Lista el contenido de la tabla que recibe
    """
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero {path}")
        else:
            # Abrir la conexión:
            con = dbapi.connect(path)
            # Crear un cursor:
            cur = con.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            cabs = sep.join([t[0] for t in cur.description])
            print(cabs)

            for t in cur.fetchall():
                print(t)

    except Exception as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def testConexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero {path}")
        else:
            # Abrir la conexión:
            con = dbapi.connect(path)
            print("Conexión abierta ...")

    except Exception as e:
        print(e)

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    # testConexion("../bd/empresa3.db")
    consulta("categorias", "../bd/empresa3.db")
