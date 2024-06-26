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


if __name__ == "__main__":
    c1 = Candidato("Ana", 9, 3, True)
    print(c1)  # print(str(c1)) # print(c1.__str__())
    print("Código: ", c1.generarCode())

    diccionarios = generarDiccionarios()
    # print(diccionarios[:3])
    candidatos = [Candidato(**d) for d in diccionarios]
    print(f"Tenemos {len(candidatos)} candidatos")
    candidatos.sort(key=lambda obj: obj.generarCode(), reverse=True)
    for c in candidatos[:10]:
        print(c)
