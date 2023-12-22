"""
Implementar las operaciones CRUD (create - read - update - delete)
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
            raise FileNotFoundError(f"El fichero {path} no existe")
        else:
            self.con = dbapi.connect(path)

    def select(self):
        """
        Devuelve una lista con los empleados
        """
        cur = None
        try:
            sql = "select * from empleados"
            cur = self.con.cursor()
            cur.execute(sql)
            L = [Empleado(*t) for t in cur.fetchall()]
            return L

        except Exception as e:
            raise e  # Relanzar excepción
        finally:
            if cur:
                cur.close()

    def read(self, id):
        """
        Recuperar un empleado de la Bd a partir del id
        """
        cur = None
        try:
            sql = "select * from empleados where id=?"
            cur = self.con.cursor()
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t:
                return Empleado(*t)
            else:
                raise ValueError(f"El empleado con id: {id} no existe")

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def create(self, empleado):
        """
        Crea un nuevo empleado en la BD.
        """
        cur = None
        try:
            sql = "insert into empleados(nombre, cargo) values(?,?)"
            cur = self.con.cursor()
            cur.execute(sql, empleado.getTupla())
            empleado.setId(cur.lastrowid)
            n = cur.rowcount  # Antes de confirmar la Transacción
            self.con.commit()
            return n

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def delete(self, id):
        """
        Borra un empleado de la BD a partir del ID
        """
        cur = None
        try:
            sql = "delete from empleados where id = ?"
            cur = self.con.cursor()
            cur.execute(sql, (id,))
            n = cur.rowcount  # Antes de confirmar la Transacción
            self.con.commit()
            if n == 0:
                raise ValueError(f"El empleado con id:{id} no existe")
            else:
                return n

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def update(self, empleado):
        """
        Actualiza el nombre y el cargo de un empleado de la BD
        """
        cur = None
        try:
            sql = "update empleados set nombre=?,cargo=? where id = ?"
            cur = self.con.cursor()
            cur.execute(sql, empleado.getTupla2())
            n = cur.rowcount  # Antes de confirmar la Transacción
            self.con.commit()
            if n == 0:
                raise ValueError(f"El empleado con id:{id} no existe")
            else:
                return n

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
        bd = EmpleadoBD("../bd/empresa3.db")
        L = bd.select()
        print(f"Tenemos {len(L)} empleados")

        e1 = bd.read(1)
        print(e1)

        e1.setCargo("Gerente")
        if bd.update(e1) == 1:
            print("Registro actualizado")

        """
        nuevo = Empleado(0, "Sandra", "Gerente")
        if bd.create(nuevo) == 1:
            print("Registro creado")
            print(nuevo)
        """

        if bd.delete(150) == 1:
            print("Registro borrado")

    except Exception as e:
        print(e)
