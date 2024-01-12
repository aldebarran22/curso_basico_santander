"""
Conectar con la BD sqlite3.
Crear conexiones y cursores. Ejecutar una consulta.
"""

import sqlite3 as dbapi
from os.path import isfile
import sys


def grabarCategoria(path, categoria):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero {path}")
        else:
            # Abrir la conexión:
            con = dbapi.connect(path)
            sql = "insert into categorias(nombre) values(?)"
            cur = con.cursor()
            cur.execute(sql, (categoria,))
            print("Número de registros creados: ", cur.rowcount)
            print("id generado: ", cur.lastrowid)
            con.commit()  # Confirmar la transacción

    except Exception as e:
        con.rollback()  # Rechazar los cambios.
        print(e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def consulta(tabla, path, sep=";", file=sys.stdout):
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
            print(cabs, file=file)

            for t in cur.fetchall():
                fila = sep.join([str(i) for i in t])
                print(fila, file=file)

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


def exportar(pathBD, *tablas, sep=";"):
    for tabla in tablas:
        fich = None
        try:
            path = f"../ficheros/{tabla}.csv"
            fich = open(path, "w")
            consulta(tabla, pathBD, sep, fich)

        except Exception as e:
            print(e)
        finally:
            if fich:
                fich.close()


if __name__ == "__main__":
    # testConexion("../bd/empresa3.db")
    # consulta("categorias", "../bd/empresa3.db")
    # exportar("../bd/empresa3.db", "clientes", "pedidos", "productos", sep=";")
    grabarCategoria("../bd/empresa3.db", "viajes")
