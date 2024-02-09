import sqlite3 as db
from os.path import isfile

def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"El fichero {path} no existe")
        else:
            con = db.connect(path)
            print('conexión ok')

    except Exception as e:
        #raise e
        print(e)
    finally:
        if con: con.close()

if __name__ == '__main__':
    conexion('../bd/empresa3.db')
