"""
Implementar las operaciones CRUD (
    create -> insert into
    read -> select pk
    update -> update pk
    delete -> delete pk
    select -> select * from empleados
para los empleados de la base de datos.
"""

from os.path import isfile
import sqlite3 as dbapi


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

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")

        self.con = dbapi.connect(path)

    def read(self, id):
        cur = None
        try:
            sql = "select * from empleados where id=?"
            cur = self.con.cursor()
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El empleado con id: {id} no existe en la BD")
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
            sql = "select * from empleados "
            if not cargo:
                cur.execute(sql)
            else:
                sql += " where cargo like ?"
                param = f"%{cargo}%"
                cur.execute(sql, (param,))

            return [Empleado(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        t = (id,)
        sql = "delete from empleados where id=?"
        return self.__update_delete(t, sql)

    def update(self, emp):
        t = emp.getTupla2()
        sql = "update empleados set nombre=?, cargo=? where id=?"
        return self.__update_delete(t, sql)

    def __update_delete(self, t, sql):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql, t)
            n = cur.rowcount
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
            emp.setId(cur.lastrowid)  # Recupera el id asignado al empleado
            n = cur.rowcount
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
            self.con.close()


if __name__ == "__main__":
    try:
        bd = EmpleadoBD("../../bd/empresa3.db")

        emp = bd.read(4)
        print(emp)
        emp.setCargo("Gerente de ventas")
        if bd.update(emp):
            print(emp, "actualizado")
        else:
            print("No se ha podido actualizar!")

        print("\nListado:")
        L = bd.select("ventas")
        for e in L:
            print(e)

        emp1 = Empleado(0, "Sandra", "Gerente de Ventas")
        if bd.create(emp1):
            print("Create ok: ", emp1)
        else:
            print("No se ha podido crear")

    except Exception as e:
        print(e)
