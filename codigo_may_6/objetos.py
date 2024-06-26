"""
POO en Python:
Diseño de clases
- Sobrecarga de operadores
- Funciones especiales 
- Listas de objetos
"""


class Persona:
    """Implementación de la clase Persona"""

    # Variable de clase:
    contador = 0

    def __init__(self, nombre="", edad=0, altura=0.0):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad

        Persona.contador += 1

    def __str__(self):
        return self.nombre + " " + str(self.altura) + " " + str(self.edad)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.edad < other.edad

    def __eq__(self, other: object) -> bool:
        for k, v in self.__dict__.items():
            if k in other.__dict__:
                if v != other.__dict__[k]:
                    return False
            else:
                return False
        return True

    def hablarCon(self, other=None):
        if other is None:
            print(self.nombre, "habla solo")
        else:
            print(self.nombre, "y", other.nombre, "están hablando")

    @staticmethod
    def getContador():
        return Persona.contador

    def __del__(self):
        Persona.contador -= 1
        # print('Se está borrando: ', self.nombre)


class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0.0, ambito="", idiomas=[]):
        Persona.__init__(self, nombre, edad, altura)
        # super().__init__(nombre, edad, altura)

        self.ambito = ambito
        self.idiomas = idiomas

    def hablarCon(self, other=None):
        if not other:
            Persona.hablarCon(self)
        else:
            c1 = set(self.idiomas)
            c2 = set(other.idiomas)

            comun = c1 & c2
            if len(comun) == 0:
                print("No tienen un idioma en común")
            else:
                print(self.nombre, "habla con", other.nombre, "en", " o ".join(comun))

    def __str__(self):
        return Persona.__str__(self) + " " + self.ambito + " " + ",".join(self.idiomas)


class Grupo:

    def __init__(self, nombre="", *personas):
        self.nombre = nombre
        self.grupo = []
        self.grupo.extend(personas)
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == len(self.grupo):
            self.indice = 0
            raise StopIteration  # Cortar el bucle for
        else:
            emp = self.grupo[self.indice]
            self.indice += 1
            return emp

    def __len__(self):
        return len(self.grupo)

    def alta(self, persona, *personas):
        self.grupo.append(persona)
        self.grupo.extend(personas)


def pruebaGrupo():
    g1 = Guia("Pedro", 45, 1.77, "N", ["inglés", "alemán"])
    p1 = Persona("Miguel", 34, 1.8)
    p3 = Persona("Ana", 32, 1.82)
    p4 = Persona("Paula", 31, 1.71)

    grupo = Grupo("Viaje1", g1)
    grupo.alta(p1, p3, p4)
    print("Num personas: ", len(grupo))
    for p in grupo:
        print(p)


def pruebaGuia():
    g1 = Guia("Pedro", 45, 1.77, "N", ["inglés", "alemán"])
    g2 = Guia("José", 55, 1.78, "I", ["italiano", "francés"])

    if g1 < g2:
        print(g1.nombre, "es menor que", g2.nombre)
    else:
        print(g2.nombre, "es menor que", g1.nombre)

    g1.hablarCon(g2)

    print(g1)


def pruebaPersona():
    p1 = Persona("Miguel", 34, 1.8)
    p3 = Persona("Ana", 32, 1.82)
    p4 = Persona("Paula", 31, 1.71)
    p2 = Persona("Eva", 44, 1.79)
    print(p1)
    # print(str(p1))
    # print(p1.__str__())

    L = [p1, p2, Persona("Jose", 15, 1.77)]
    print(L)

    print("La clase del objeto: ", p1.__class__.__name__)
    print("Dic:", p1.__dict__)
    p1.tno = 915674433
    p1.__dict__["movil"] = 678456788
    print("Dic:", p1.__dict__)

    L.sort(reverse=True)
    print(L)
    if p1 < p2:
        print(p1.nombre, "es menor que", p2.nombre)
    else:
        print(p2.nombre, "es menor que", p1.nombre)

    if p1 > p2:
        print(p1.nombre, "es mayor que", p2.nombre)
    else:
        print(p2.nombre, "es mayor que", p1.nombre)

    if p4 == p3:
        print("iguales")
    else:
        print("no iguales")

    p1.hablarCon()
    p1.hablarCon(p2)

    # Ordenar por al altura DESC:
    L.sort(key=lambda obj:obj.altura, reverse=True)
    print(L)
    L.sort(key=lambda obj:obj.nombre)
    print(L)

def pruebaStatic():
    print("Num instancias:", Persona.getContador())
    p1 = Persona("Miguel", 34, 1.8)
    print("Num instancias:", Persona.getContador())
    p2 = Persona("Miguel", 34, 1.8)
    p3 = Persona("Miguel", 34, 1.8)
    print("Num instancias:", Persona.getContador())
    del p1  # llama al destructor de la clase: __del__
    print("Num instancias:", Persona.getContador())


if __name__ == "__main__":
    pruebaPersona()
    # pruebaGuia()
    # pruebaStatic()
    # pruebaGrupo()
