"""
POO en Python. Definición de clases
"""

from modulos.persona import Persona
from modulos.guia import Guia
from modulos.grupo import Grupo


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
    L2 = [o.__dict__ for o in L]
    print(L2)
    print(g1.__class__)
    obj = g1.__class__("Felipe", ambito="I")
    print(obj)


def testGrupo():
    g = Grupo("Grupo Navidad", "Ana", "Miguel")
    g.addPersona("Isabel", "Gema")
    print(len(g), "personas")
    for i in g:
        print(i, end=" ")
    for i in g:
        print(i, end=" ")


def testPersona2():
    p = Persona("Ana", 34, 1.8)
    p.__dict__["apellido"] = "Sanz"
    p.__dict__["telefono"] = 699887788
    p.calle = "Gran Via"
    print(p)


if __name__ == "__main__":
    testPersona()
    testGuia()
    testGrupo()
    testPersona2()
