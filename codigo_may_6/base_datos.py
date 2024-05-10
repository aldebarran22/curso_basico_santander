"""
Conectar con la BD sqlite3. Crear conexiones, cursores, exportar datos

CRUD:
Create -> insert into
Read -> select (pk)
Update -> update (pk)
delete -> delete (pk)
select
"""

import sqlite3 as db
import sys
from os.path import isfile


def conexion(path, tabla, file=sys.stdout, sep=";"):
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
            fila = sep.join(
                [
                    str(i).replace(".", ",") if isinstance(i, float) else str(i)
                    for i in t
                ]
            )
            print(fila, file=file)

    except Exception as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def exportar(path, tabla, sep=";"):
    path_file = f"../ficheros/{tabla}.csv"
    fich = open(path_file, "w")
    conexion(path, tabla, fich, sep)
    fich.close()


def testExportar():
    conexion("../../bd/empresa3.db", "pedidos")
    exportar("../../bd/empresa3.db", "pedidos")


class Categoria:

    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)


class Producto:

    def __init__(self, id=0, nombre="", precio=0.0, exis=0, cat=Categoria()):
        self.id = id
        self.nombre = nombre
        self.cat = cat
        self.precio = round(precio, 2)
        self.exis = exis

    def __str__(self):
        return (
            str(self.id)
            + " "
            + self.nombre
            + " "
            + str(self.cat)
            + " "
            + str(self.precio)
            + " "
            + str(self.exis)
        )

    def __repr__(self):
        return str(self)

    def getTupla(self):
        return (self.nombre, self.cat.id, self.precio, self.exis)

    def getTupla2(self):
        return (self.nombre, self.cat.id, self.precio, self.exis, self.id)


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        self.con = db.connect(path)

    def deleteProducto(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "delete from productos where id=?"
            cur.execute(sql,(id,))
            n = cur.rowcount
            self.con.commit()
            return n == 1
                        
        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def createCategoria(self, categoria):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "insert into categorias(nombre) values(?)"
            cur.execute(sql, (categoria.nombre,))
            categoria.id = cur.lastrowid
            n = cur.rowcount
            self.con.commit()
            return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def selectCategorias(self):
        """Devuelve una col. de objetos categoria"""
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from categorias"
            cur.execute(sql)
            return [Categoria(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __getProducto(self, t):
        cat = Categoria(*t[-2:])
        tuplaProd = t[:-2]
        tp = tuplaProd + (cat,)
        return Producto(*tp)

    def selectProductos(self, categoria=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idprod, p.nombre as nombreProd,
            p.precio, p.existencias, c.id as idcat, 
            c.nombre as nombrecat from categorias c
             inner join productos p on c.id = p.idcategoria"""
            if categoria:
                # Filtro de la categoria:
                sql += " where c.nombre = ? order by c.nombre, p.nombre"
                cur.execute(sql, (categoria,))
            else:
                sql += " order by c.nombre, p.nombre"
                cur.execute(sql)

            return [self.__getProducto(t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:
                cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


def borrarProducto():
    try:
        bd = BaseDatos("../../bd/empresa3.db")
        id = int(input("Dame producto: "))
        if bd.deleteProducto(id):
            print("Se ha borrado el producto: ", id)
        else:
            print("No se ha podido borrar")

    except Exception as e:
        print(e.__class__.__name__, e)


def testBaseDatos():
    try:
        bd = BaseDatos("../../bd/empresa3.db")
        categorias = bd.selectCategorias()
        print(categorias)

        productos = bd.selectProductos("Carnes")
        for p in productos:
            print(p)

        nuevaCat = Categoria(nombre="Viajes")
        if bd.createCategoria(nuevaCat):
            print(nuevaCat)
        else:
            print("No se ha podido crear...")

        if bd.deleteProducto(83):
            print("producto borrado")
        else:
            print("no se ha borrado")

    except Exception as e:
        print(e.__class__.__name__, e)


if __name__ == "__main__":
    # testBaseDatos()
    borrarProducto()
