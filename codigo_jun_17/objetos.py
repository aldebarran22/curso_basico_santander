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


if __name__ == '__main__':
    p1 = Producto(1, "CocaCola", 1, 1.5, 100)
    print(p1)
