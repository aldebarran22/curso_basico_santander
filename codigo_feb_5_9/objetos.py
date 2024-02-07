"""
POO en Python
"""


class Persona:
    """
    Implementar la clase Persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definición de atributos:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if not otro:
            print(self.nombre, "está hablando solo")
        else:
            print(f"{self.nombre} y {otro.nombre} están hablando")

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __del__(self):
        # print('se borra a ', self.nombre)
        pass


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        # Forma 1:
        Persona.__init__(self, nombre, edad, altura)
        # Forma 2:
        # super().__init__(nombre, edad, altura)

        # Atributos de la clase Guia:
        self.ambito = ambito
        self.idiomas = idiomas

    def hablarCon(self, otro=None):
        if not otro:
            Persona.hablarCon(self, otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            comunes = c1 & c2
            if len(comunes) == 0:
                print("No pueden hablar ...")
            else:
                print(
                    self.nombre,
                    "y",
                    otro.nombre,
                    " pueden hablar en:",
                    " o ".join(comunes),
                )

    def __str__(self):
        # return Persona.__str__(self)
        return super().__str__() + " " + self.ambito + " " + ",".join(self.idiomas)


def testPersona():
    p1 = Persona("Pedro", 45, 1.9)
    p2 = Persona("Sara", 40, 1.88)
    p1.hablarCon()
    p1.hablarCon(p2)

    # del(p1) Se fuerza la llamada al destructor de la clase: __del__

    if p2 < p1:  # if p2.__lt__(p1)
        print(p2.nombre, "es menor que", p1.nombre)
    else:
        print(p1.nombre, "es menor que", p2.nombre)

    L = [p1, p2, Persona("Ana", 42, 1.85)]
    L.sort(reverse=True)
    print(L)
    L.sort(key=lambda obj: obj.altura)
    print(L)

    print("p1 pertenece a la clase: ", p1.__class__.__name__)
    p2 = p1.__class__()  # Crea un nuevo objeto
    print(p2, type(p2))

    # print(str(p1))
    # print(p1.__str__())


def testGuia():
    g1 = Guia("Sandra", 34, 1.8, "I", ["inglés", "alemán"])
    g2 = Guia("Juan", 32, 1.78, "N", ["francés", "alemán", "inglés"])

    print(g1)
    g1.cumple()
    print(g1)
    g1.hablarCon(g2)


if __name__ == "__main__":
    # testPersona()
    testGuia()
