"""POO en Python."""


class Persona:
    """Implementación de la clase persona"""

    # Att de clase:
    numPersonas = 0

    def __init__(self, nombre="", edad=0, altura=0.0):
        # Definir att de la clase:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

        Persona.numPersonas += 1

    """
    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)
    """

    @staticmethod
    def getNumPersonas():
        return Persona.numPersonas

    def __str__(self):
        resul = ""
        for k, v in self.__dict__.items():
            resul += str(v) + " "
        return resul

    def __repr__(self):
        return str(self)  # return self.__str__()

    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False

    def __eq__(self, other):
        return (
            self.nombre == other.nombre
            and self.edad == other.edad
            and self.altura == other.altura
        )

    def hablarCon(self, other=None):
        if not other:
            print("La persona está hablando sola")
        else:
            print(self.nombre, "habla con", other.nombre)

    def cumpleaños(self):
        self.edad += 1

    def __del__(self):
        Persona.numPersonas -= 1
        # print("Eliminando a: ", self.nombre)


class Empleado(Persona):

    def __init__(
        self, nombre="", edad=0, altura=0.0, empresa="", sueldo=0.0, idiomas=[]
    ):
        # Llamar al constructor de la clase padre: Persona
        # Persona.__init__(self, nombre, edad, altura)
        super().__init__(nombre, edad, altura)

        # Definir los att. de la clase Empleado:
        self.empresa = empresa
        self.sueldo = sueldo
        self.idiomas = idiomas

    def hablarCon(self, other=None):
        if not other:
            super().hablarCon(other)
        else:
            c1 = set(self.idiomas)
            c2 = set(other.idiomas)

            comun = c1 & c2
            if len(comun) == 0:
                print('No pueden hablar')
            else:
                print('Pueden hablar en: ', " o ".join(comun))


def testPersona():
    print("NumPersonas. ", Persona.getNumPersonas())
    p1 = Persona("Ana", 47, 1.76)
    p2 = Persona("Pedro", 46, 1.75)
    p3 = Persona("Juan", 45, altura=1.82)
    person1 = Persona("Angel")
    print("NumPersonas. ", Persona.getNumPersonas())
    del person1
    print("NumPersonas. ", Persona.getNumPersonas())

    if p1 == p2:
        print("p1 y p2 son iguales")
    else:
        print("Son distintos")

    L = [p1, p2, p3, Persona("Sonia", 23, 1.77)]
    print(L)
    # Ordenar por Edad ASC
    L.sort(key=lambda obj: obj.edad)
    print(L)
    # Ordenar por altura DESC
    L.sort(key=lambda obj: obj.altura, reverse=True)
    print(L)

    L.sort()
    print("L.sort() -> ", L)

    # print(str(p1))
    # print(p1.__str__())

    print(p1.__dict__)
    p1.__dict__["tno"] = 912233445
    p1.movil = 600455654
    print(p1.__dict__)
    del p1.nombre  # Borra el att
    print(p1)
    print(p1.__class__)
    print(p1.__class__.__name__)

    # Crear objetos:
    persona1 = p1.__class__("Jorge")
    print(persona1)


def testEmpleado():
    emp1 = Empleado("Sandra", 44, 1.77, "Santander", 2000.0, ["inglés", "francés"])
    emp2 = Empleado("Eva", 42, 1.78, "TTR", 2200.0, ["inglés", "alemán"])
    emp1.hablarCon(emp2)
    emp2.cumpleaños()

    if emp1 < emp2:
        print(emp1.nombre, "es menor que", emp2.nombre)
    else:
        print(emp2.nombre, "es menor que", emp1.nombre)

    L = [emp1, emp2, Empleado("Juan", 46, 1.76, "DDR", 1500.0)]
    L.sort()
    print(L)


if __name__ == "__main__":
    # testPersona()
    testEmpleado()
