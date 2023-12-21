try:
    from modulos.persona import Persona
except: 
    from persona import Persona


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
