
class TimeError(Exception):
    """Gestión de errores de la hora"""

    def __init__(self, msg=""):
        super().__init__(msg)
        # Exception.__init__(self, msg)


class Time:

    # Att. de clase:
    num_instancias = 0

    def __init__(self, h=0, m=0, s=0):

        if not (0 <= s <= 59):
            raise TimeError(f"El valor de los sg: {s} no es correcto")

        if not (0 <= m <= 59):
            raise TimeError(f"El valor de los min: {m} no es correcto")
        
        if not (0 <= h <= 23):
            raise TimeError(f"El valor de las horas: {h} no es correcto")

        self.h = h
        self.m = m
        self.s = s

        Time.num_instancias += 1

    def __ajustar(self):
        minutos = self.s // 60
        self.s %= 60

        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h = (self.h + horas) % 24

    @staticmethod
    def getNumInstancias():
        return Time.num_instancias

    @classmethod
    def getNumInstancias2(cls):
        return Time.num_instancias

    def __add__(self, other):
        obj = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        obj.__ajustar()
        return obj

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

    def __repr__(self):
        return str(self)

    def __del__(self):
        Time.num_instancias -= 1
