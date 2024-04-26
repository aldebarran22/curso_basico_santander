"""
Implementación de las operaciones CRUD:
Create -> insert into
Read -> select (pk)
Update -> update
Delete -> delete
select (categoria=None)
"""
import sqlite3 as db
from os.path import isfile

class Categoria:

    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)


class Producto:

    def __init__(self, id=0, nombre="", cat=Categoria(), precio=0.0, exis=0):
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

class ProductoCRUD:

    def __init__(self, path):

        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            self.con = db.connect(path)

    def __getProducto(self, t):
            cat = Categoria(*t[2:4])               
            t2 = t[:2]+(cat,)+t[4:]
            prod = Producto(*t2)
            return prod

    def read(self, pk):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idp, p.nombre, c.id as idc, c.nombre as nombrecat, 
            p.precio, p.existencias from productos p inner join categorias c 
            on p.idcategoria = c.id where p.id = ?"""
            cur.execute(sql, (pk,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El producto con pk: {pk} no existe en la BD")
            else:
               return self.__getProducto(t)

        except Exception as e:
            raise e
        finally:
            if cur:cur.close()

    def select(self, categoria=None):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idp, p.nombre, c.id as idc, c.nombre as nombrecat, 
            p.precio, p.existencias from productos p inner join categorias c 
            on p.idcategoria = c.id"""
            if categoria:
                sql += " where c.nombre = ?"
                cur.execute(sql, (categoria,))

            else:
                cur.execute(sql)

            return [self.__getProducto(t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur:cur.close()

    def update(self, prod):
        sql = "update productos set nombre=?, idcategoria=?, precio=?, existencias=? where id=?"
        t = prod.getTupla2()
        pk = prod.id
        return self.__actualizar(sql, t, pk)

    def delete(self, pk):
        sql = "delete from productos where id=?"
        return self.__actualizar(sql, (pk,), pk)

    def __actualizar(self, sql, t, pk):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql, t)
            n = cur.rowcount
            self.con.commit()
            if n == 0:
                raise ValueError(f"El producto con pk: {pk} no existe en la BD")
            else:
                return n == 1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:cur.close()

    def create(self, prod):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "insert into productos(nombre, idcategoria, precio, existencias) values(?,?,?,?)"
            cur.execute(sql, prod.getTupla())
            n = cur.rowcount
            prod.id = cur.lastrowid
            self.con.commit()
            return n==1

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:cur.close()

    def __del__(self):
        if hasattr(self, 'con'):
            self.con.close()

if __name__=='__main__':
    try:
        bd = ProductoCRUD('../bd/empresa3.db')
        obj = bd.read(12)
        print(obj)

        L = bd.select()
        #L = bd.select("Bebidas")
        for prod in L:
            print(prod)

        """
        nuevo = Producto(0, 'CocaCola10', Categoria(1,'Bebidas'),2.5, 100)
        if bd.create(nuevo):
            print('Producto creado: ', nuevo)
        else:
            print('No se ha creado')

        obj = bd.read(86)
        print(obj)
        obj.precio = 20.0
        obj.exis = 200
        if bd.update(obj):
            print('Producto actualizado')
        else:
            print('No se ha podido actualizar')
        """
       
        
        if bd.delete(86):
            print('producto borrado')
        else:
            print('no se ha borrado')
        

    except Exception as e:
        print(e)
