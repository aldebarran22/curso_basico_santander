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


class EmpleadoCRUD:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            self.con = db.connect(path)

    def update(self, emp):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "update empleados set nombre=?, cargo=? where id = ?"
            cur.execute(sql, emp.getTupla2())
            n = cur.rowcount  # Número de registros afectado
            if n == 0:
                raise ValueError(f"No existe el empleado: {emp.id}")
            else:
                self.con.commit()
                return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "delete from empleados where id = ?"
            cur.execute(sql, (id,))
            n = cur.rowcount  # Número de registros afectado
            if n == 0:
                raise ValueError(f"No existe el empleado: {id}")
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
            sql = "insert into empleados(nombre,cargo) values(?,?)"
            cur.execute(sql, emp.getTupla())
            n = cur.rowcount  # Número de registros afectado
            emp.setId(cur.lastrowid)  # Obtener y colocar el id asignado
            self.con.commit()
            return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from empleados where id=?"
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t:
                return Empleado(*t)
            else:
                raise ValueError(f"No existe el empleado: {id}")

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def select(self):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from empleados"
            cur.execute(sql)
            return [Empleado(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        path = "../bd/empresa3.db"
        bd = EmpleadoCRUD(path)

        L = bd.select()
        print(len(L), "empleados")

        emp = bd.read(2)
        print(emp)
        emp.setCargo("Gerente de Ventas")
        if bd.update(emp):
            print("Se ha actualizado el registro")

        """
        if bd.delete(16):
            print("Registro eliminado")

        if bd.delete(100):
            print("Registro eliminado")

        
        emp2 = Empleado(0, "Robert", "Representante de Ventas")
        if bd.create(emp2):
            print("Id asignado: ", emp2.getId())
        """

    except Exception as e:
        print(e.__class__.__name__, e)
