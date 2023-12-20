"""
POO en Python. Definición de clases
"""


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
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        pass
        # print("Se está eliminando a: ", self.nombre)


class Guia(Persona):
    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)
        self.ambito = ambito
        self.idiomas = idiomas

    def __str__(self):
        return super().__str__() + " " + self.ambito + " " + ",".join(self.idiomas)

    def hablarCon(self, otro=None):
        # Comprobar si tienen un idioma en común
        if not otro:
            return super().hablarCon(otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            comun = c1 & c2
            if len(comun) == 0:
                raise Exception("No tienen un idioma en común")
            else:
                print(self.nombre, "y", otro.nombre, "pueden hablar en", comun)


def testPersona():
    p1 = Persona("Sandra", 30, 1.7)
    p2 = Persona("Jose", 44, 1.76)
    print(p1.nombre)
    p1.nombre = "Eva"
    # del(p1) # Fuerza la llamada al destructor: __del__
    print(p1)
    # print(str(p1))
    # print(p1.__str__())
    p1.cumple()  # objeto.metodo()
    p2.hablarCon()
    p2.hablarCon(p1)
    L = [p1, p2, Persona("Miguel", 23, 1.8)]
    print(L)
    L.sort(key=lambda p: p.nombre)
    print(L)
    L.sort()
    print(L)


def testGuia():
    g1 = Guia("Ana", 34, 1.77, "I", ["inglés", "alemán"])
    g2 = Guia("Sonia", 32, 1.87, "N", ["inglés", "francés", "alemán"])
    g3 = Guia("Victor", 28, 1.85, "L", ["inglés"])
    print(g1)
    g1.cumple()
    print(g1)
    g1.hablarCon(g2)
    L = [g1, g2, g3]
    L.sort()
    print(L)
    g1.hablarCon(g2)


if __name__ == "__main__":
    # testPersona()
    testGuia()
