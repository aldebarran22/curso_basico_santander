class Persona:
    """
    Clase persona. Propiedades y métodos
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if otro:
            print(self.nombre, "habla con ", otro.nombre)
        else:
            print(self.nombre, "habla solo")

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "\n".join([k + "=" + str(v) for k, v in self.__dict__.items()])
        # return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        pass
        # print("Se está eliminando a: ", self.nombre)
