"""
Conectar con la bd de sqlite3 y extraer registros (exportar a ficheros)
"""

import sqlite3 as db
from os.path import isfile

def listarTabla(path, tabla, sep=";"):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            # Abrir la conexión con la BD:
            con = db.connect(path)
            #print("conexión ok")

            # Crear un cursor:
            cur = con.cursor()

            # Definir el SQL:
            sql = f"select * from {tabla}"

            # Ejecutar el SQL:
            cur.execute(sql)

            # Extraer los nombres de las columnas
            cabs = sep.join([t[0] for t in cur.description])
            print(cabs)

            # Recorrer los resultados
            for t in cur.fetchall():
                datos = sep.join([str(i) for i in t])
                print(datos)

    except Exception as e:
        raise e
    finally:
        if cur: cur.close()
        if con: con.close()

if __name__=='__main__':
    try:
        listarTabla("../bd/empresa3.db", "categorias")
    except Exception as e:
        print(e.__class__.__name__, e)
