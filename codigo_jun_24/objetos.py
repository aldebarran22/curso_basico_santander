"""
POO en Python
"""


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


if __name__ == "__main__":
    c1 = Candidato("Ana", 9, 3, True)
    print(c1)  # print(str(c1)) # print(c1.__str__())
