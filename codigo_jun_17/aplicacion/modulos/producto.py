


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