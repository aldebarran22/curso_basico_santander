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

    def __del__(self):
        # print("borrando: ", self.nombre)
        pass


if __name__ == "__main__":
    p1 = Producto(1, "CocaCola", 1, 1.5, 100)
    # del(p1) fuerza la llamada al destructor!
    print(p1)  # print(p1.__str__())

    p2 = Producto(2, "Fanta limón", 1, 1.25, 200)
    print(p2)

    L = [p1, p2, Producto(3,"Pan",2,1.0, 10)]
    print(L)
