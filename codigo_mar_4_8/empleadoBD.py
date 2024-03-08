"""
Implementar las operaciones CRUD para una entidad
de la base de datos
C - Create: insert into
R - Read: select ... where id=PK
U - Update: update
D - Delete: delete
select: select all
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


class EmpleadoBD:
    """Implementar las operaciones CRUD"""

    def __init__(self, path):

        if not isfile(path):
            raise FileNotFoundError(f"No existe la BD: {path}")

        self.con = db.connect(path)

    def select(self, cargo=None):
        cur = None
        try:
            sql = "select * from empleados"
            cur = self.con.cursor()
            if cargo:
                param = f"'%{cargo}%'"
                sql += " where cargo like " + param

            cur.execute(sql)

            return [Empleado(*t) for t in cur.fetchall()]
        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def read(self, id):
        cur = None
        try:
            sql = "select * from empleados where id=?"
            cur = self.con.cursor()
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El empleado {id} no existe")
            else:
                return Empleado(*t)

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        cur = None
        try:
            sql = "delete from empleados where id=?"
            cur = self.con.cursor()
            cur.execute(sql, (id,))
            n = cur.rowcount
            self.con.commit()
            if n == 0:            
                raise ValueError(f"El empleado {id} no se ha podido eliminar")
            return True
        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        empBD = EmpleadoBD("../bd/empresa3.db")
        L = empBD.select("Representante")
        print(L)

        emp = empBD.read(1)
        print(emp)

        if empBD.delete(7):
            print('registro eliminado')

        emp2 = Empleado(0, 'Juan', 'Representante de Ventas')
        if empBD.create(emp2):
            print('nuevo empleado: ', emp2)

    except Exception as e:
        print(e)
