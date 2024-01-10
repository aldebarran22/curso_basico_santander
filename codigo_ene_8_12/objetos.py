"""
Diseño orientado a objetos en Python
Implementar clases y utilización
Colecciones de objetos
"""


class Persona:
    """
    Implementación de la clase persona
    """

    def __init__(self, nombre="", edad=0, altura=0.0):
        # definir att.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def cumple(self):
        self.edad += 1

    def hablarCon(self, otro=None):
        if otro != None:
            print(self.nombre, "habla con", otro.nombre)
        else:
            print(self.nombre, "habla solo")

    def __lt__(self, other):
        return self.edad < other.edad

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

    def __repr__(self):
        # Vuelve a llamar al método __str__()
        return str(self)


class Guia(Persona):
    """
    Clase guia turístico.
    """

    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        # Llamar al constructor de la clase Padre:
        Persona.__init__(self, nombre, edad, altura)
        # Otra forma para hacer lo mismo:
        # super().__init__(nombre, edad, altura)

        # definir los atributos del Guia:
        self.ambito = ambito
        self.idiomas = idiomas

    def hablarCon(self, otro=None):
        if otro == None:
            # Llamar al método de la clase Padre
            Persona.hablarCon(self, otro)
        else:
            c1 = set(self.idiomas)
            c2 = set(otro.idiomas)
            comunes = c1 & c2
            if len(comunes) > 0:
                print(self.nombre, "habla con", otro.nombre, "en", comunes)
            else:
                print("No pueden hablar, no tienen un idioma común")

    def __str__(self):
        # Reutilizamos el método __str__ de la clase Persona
        return Persona.__str__(self) + " " + self.ambito + " " + ",".join(self.idiomas)


def testPersona():
    p1 = Persona("Pedro", 33, 1.8)
    p2 = Persona("Juan", 30, 1.82)
    p1.hablarCon()
    p1.hablarCon(p2)
    if p1 < p2:  # if p1.__lt__(p2)
        print(p1, "menor que", p2)
    else:
        print(p2, "menor que", p1)
    print(p1)
    p1.cumple()
    print(p1)
    # print(str(p1))
    # print(p1.__str__())
    L = [p1, Persona("Ana", 14, 1.77), Persona("Sara", 13, 1.88)]
    print(L)
    L.sort(key=lambda obj: obj.altura, reverse=True)
    print(L)
    L.sort()
    print(L)


def testGuia():
    g1 = Guia("Andrés", 33, 1.8, "I", ["inglés", "francés"])
    g2 = Guia("Ana", 32, 1.78, "I", ["italiano", "inglés", "francés"])
    print(g1)
    g1.cumple()
    print(g1)
    g1.hablarCon()


if __name__ == "__main__":
    # testPersona()
    testGuia()
