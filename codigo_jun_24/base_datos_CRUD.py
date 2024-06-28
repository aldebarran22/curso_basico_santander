"""
Implementar las operaciones CRUD de una entidad de la base de datos:
C - Create -> insert into
R - Read -> select (pk)
U - Update -> update (pk)
D - Delete -> delete (pk)

select 
"""

import sqlite3 as db
from os.path import isfile


class Empleado:
    def __init__(self, id=0, nombre="", cargo=""):
        self.__id = id
        self.__nombre = nombre
        self.__cargo = cargo

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getTupla(self):
        return (self.__nombre, self.__cargo)

    def getTupla2(self):
        return (self.__nombre, self.__cargo, self.__id)

    def __str__(self):
        return str(self.__id) + " " + self.__nombre + " " + self.__cargo

    def __repr__(self):
        return str(self)


class EmpleadoCRUD:
    """Operaciones CRUD para un empleado"""

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No se ha encontrado el fichero: {path}")
        else:
            self.con = db.connect(path)

    def select(self, cargo=None):
        cur = None
        try:
            cur = self.con.cursor()
            if not cargo:
                sql = "select * from empleados"            
                cur.execute(sql)
            else:
                param = f"%{cargo}%"
                sql = "select * from empleados where cargo like ?"
                cur.execute(sql, (param,)) 
                
            return [Empleado(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            print("cerrando conexión...")
            self.con.close()
        else:
            print("no existe el att con")


if __name__ == "__main__":
    try:
        bd = EmpleadoCRUD("../../bd/empresa3.db")
        # del(bd) -> lanza el destructor!

        L = bd.select("Gerente")
        print("Empleados: ", len(L))
        print(L[:3])

    except Exception as e:
        print(e)
