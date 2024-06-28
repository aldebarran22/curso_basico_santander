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

    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from empleados where id=?"
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"No existe el empleado con clave: {id}")
            else:
                return Empleado(*t)

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def select(self, cargo=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from empleados"

            if not cargo:
                cur.execute(sql)
            else:
                param = f"%{cargo}%"
                sql += " where cargo like ?"
                cur.execute(sql, (param,))

            return [Empleado(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        sql = "delete from empleados where id = ?"
        t = (id,)
        return self.__delete_update(sql, t)

    def update(self, emp):
        sql = "update empleados set nombre=?, cargo=? where id=?"
        t = emp.getTupla2()
        return self.__delete_update(sql, t)

    def __delete_update(self, sql, t):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql, t)
            n = cur.rowcount
            if n == 0:
                raise ValueError(f"No existe el empleado con clave: {id}")
            else:
                self.con.commit()
                return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def create(self, emp):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "insert into empleados(nombre, cargo) values(?,?)"
            cur.execute(sql, emp.getTupla())
            n = cur.rowcount
            nuevo_id = cur.lastrowid
            emp.setId(nuevo_id)
            self.con.commit()
            return n == 1

        except Exception as e:
            self.con.rollback()
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

        L = bd.select()
        print("Empleados: ", len(L))
        print(L[:3])

        emp = bd.read(1)
        print(emp)

        # Dar de alta un nuevo empleado:
        emp2 = Empleado(0, "Miguel", "Representante de Ventas")
        if bd.create(emp2):
            print("Se ha grabado: ", emp2)
        else:
            print("No se ha creado")

    except Exception as e:
        print(e)
