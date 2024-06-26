"""
POO en Python
"""

from string import ascii_letters
from random import randint


def generarDiccionarios():
    candidatos = [
        {
            "nombre": letra * 5,
            "exp": randint(6, 10),
            "emp": randint(4, 6),
            "sup": randint(1, 10) % 2 == 0,
        }
        for letra in ascii_letters
    ]
    return candidatos


class Candidato:
    """
    Implementación de la clase Candidato
    """

    def __init__(self, nombre="", exp=0, emp=0, sup=False):
        # Definir los atributos de la clase
        self.nombre = nombre
        self.exp = exp
        self.emp = emp
        self.sup = sup

    def __eq__(self, other):
        return self.generarCode() == other.generarCode()

    def __lt__(self, other):
        cod1 = self.generarCode()
        cod2 = other.generarCode()

        return True if cod1 < cod2 else False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            self.nombre
            + " exp:"
            + str(self.exp)
            + " emp:"
            + str(self.emp)
            + " sup:"
            + str(self.sup)
        )

    def generarCode(self):
        codigo = "%d%d%d" % (self.exp, self.emp, self.sup)
        return int(codigo)


class Traductor(Candidato):

    def __init__(self, nombre="", exp=0, emp=0, sup=False, idiomas=[]):
        Candidato.__init__(self, nombre, exp, emp, sup)
        self.idiomas = idiomas


def testTraductor():
    t1 = Traductor("Sara", 10, 4, True, ["inglés", "italiano"])
    print(t1)
    print(t1.generarCode())


def testCandidato():
    c1 = Candidato("Ana", 9, 3, True)
    print(c1)  # print(str(c1)) # print(c1.__str__())
    print("Código: ", c1.generarCode())
    c2 = Candidato("José", 7, 4, False)
    print("Código: ", c2.generarCode())
    c3 = Candidato("Raquel", 7, 4, False)

    if c3 == c2:
        print("Tienen la misma puntuación")
    else:
        print("no igual")

    if c1 < c2:  # if c1.__lt__(c2):
        print(c1.nombre, "tiene menos puntuación que", c2.nombre)
    else:
        print(c2.nombre, "tiene menos puntuación que", c1.nombre)

    diccionarios = generarDiccionarios()
    # print(diccionarios[:3])
    candidatos = [Candidato(**d) for d in diccionarios]
    print(f"Tenemos {len(candidatos)} candidatos")
    # candidatos.sort(key=lambda obj: obj.generarCode(), reverse=True)
    candidatos.sort(reverse=True)
    print(candidatos[:3])

    # Ordenar por nombre:
    candidatos.sort(key=lambda obj: obj.nombre)
    print(candidatos[:3])


if __name__ == "__main__":
    # testCandidato()
    testTraductor()
