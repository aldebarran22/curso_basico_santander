"""
POO en Python
"""


class Producto:
    """
    Implementación de la clase Producto
    """

    def __init__(self, id=0, nombre="", idcategoria=0, precio=0.0, existencias=0):
        self.id = id
        self.nombre = nombre
        self.idcategoria = idcategoria
        self.precio = precio
        self.existencias = existencias

    def __str__(self):
        return (
            str(self.id)
            + " "
            + self.nombre
            + " "
            + str(self.idcategoria)
            + " "
            + str(self.precio)
            + " "
            + str(self.existencias)
        )

    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.precio < other.precio

    def __del__(self):
        # print("borrando: ", self.nombre)
        pass

class Tienda:

    def __init__(self, *prod):
        self.productos = []
        self.productos.extend(prod)
        self.indice = 0

    def __len__(self):
        return len(self.productos)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == len(self.productos):
            self.indice = 0
            raise StopIteration
        else:
            p = self.productos[self.indice]
            self.indice += 1
            return p
        



def testTienda():
    p1 = Producto(1, "CocaCola", 1, 1.5, 100)
    p2 = Producto(2, "Fanta limón", 1, 1.85, 200)
    t1 = Tienda(p1, p2)
    print("Tenemos ",len(t1),"productos")
    for p in t1:
        print(p)
    
    
def testProducto():
    p1 = Producto(1, "CocaCola", 1, 1.5, 100)
    # del(p1) fuerza la llamada al destructor!
    print(p1)  # print(p1.__str__())

    p2 = Producto(2, "Fanta limón", 1, 1.85, 200)
    print(p2)

    L = [p1, p2, Producto(3, "Pan", 2, 1.0, 10)]
    print(L)
    L.sort(reverse=True)
    print(L)
    L.sort(key=lambda obj : obj.nombre)
    print(L)
    exit()

    if p1 < p2:  # if p1.__lt__(p2):
        print(p1.nombre, "mas barato", p2.nombre)
    else:
        print(p2.nombre, "mas barato", p1.nombre)

    p1.iva = round(p1.precio * .21, 2)
    print(p1.__dict__)

    L2 = []
    for pro in L:
        L2.append(pro.__dict__)
    print(L2)

    print(p1.__class__)
    p3 = p1.__class__(nombre="patatas", precio=2.21)
    print(p3)

    

if __name__ == "__main__":
    testProducto()
    #testTienda()
