"""
Conexión a la BD, ejecutar consultas
EmpleadoCRUD
C: Create --> insert into
R: Read --> select (pk)
U: Update 
D: Delete 
"""

import sqlite3 as db
from os.path import isfile
import sys
from objetos import Empleado

def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        con = db.connect(path)
        print('Conexión ok!')

    except Exception as e:
        raise e
    finally:
        if con: con.close()

def printTabla(path, tabla, file=sys.stdout, sep=";"):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        con = db.connect(path)
        cur = con.cursor()

        sql = f"select * from {tabla}"
        cur.execute(sql)

        cabs = sep.join([t[0] for t in cur.description])
        print(cabs, file=file)
        for t in cur.fetchall():
            fila = sep.join([str(i).replace(".",",") \
                if isinstance(i,float) else str(i) for i in t])
            print(fila, file=file)

    except Exception as e:
        raise e
    finally:
        if cur: cur.close()
        if con: con.close()

def exportarTabla(path, tabla, sep=";"):
    path_file = f"../ficheros/{tabla}.csv"
    fich = open(path_file, "w")
    printTabla(path, tabla, file=fich, sep=sep)
    fich.close()


class EmpleadoCRUD:
    """Operaciones del empleado en la BD: C, R, U, D"""

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        self.con = db.connect(path)

    def read(self, pk):
        """Recupera un empleado a través de su clave primaria"""
        cur = None
        try:
            sql = "select * from empleados where id=?"
            cur = self.con.cursor()
            cur.execute(sql, (pk,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El empleado con clave: {pk} no existe en la BD")
            else:
                return Empleado(*t)

        except Exception as e:
            raise e

        finally:
            if cur:cur.close()

    def select(self, cargo=None):
        """Recupera una colección de empleados de la base de datos"""

        cur = None
        try:
            sql = "select * from empleados"
            cur = self.con.cursor()

            if not cargo:
                # Quieren todos
                cur.execute(sql)
            else:
                param = f"%{cargo}%"
                sql += " where cargo like ?"
                cur.execute(sql, (param,))

            return [Empleado(*t) for t  in cur.fetchall()]

        except Exception as e:
            raise e

        finally:
            if cur:cur.close()

        

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


def testFunciones():
    try:
        #conexion("../../empresa3.db")
        #printTabla("../../empresa3.db", "categorias")
        exportarTabla("../../empresa3.db", "pedidos")
    except Exception as e:
        print(e)

def testClases():
    try:
        bd = EmpleadoCRUD("../../empresa3.db")
        emp = bd.read(1)
        print(emp)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    testClases()
    