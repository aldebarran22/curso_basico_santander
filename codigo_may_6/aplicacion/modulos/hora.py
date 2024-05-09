

class TimeError(Exception):

    def __init__(self, mensaje=""):
        Exception.__init__(self, mensaje)


class Time:

    def __init__(self, hh=0, mm=0, ss=0):

        if not (0 <= hh <= 23):
            raise TimeError(f"No es correcto el valor: {hh} para las horas")

        if not (0 <= mm <= 59):
            raise TimeError(f"No es correcto el valor: {mm} para los minutos")

        if not (0 <= ss <= 59):
            raise TimeError(f"No es correcto el valor: {ss} para las sg")

        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    @staticmethod
    def __ajustar(h, m, s):
        minutos = s // 60
        s %= 60

        m += minutos
        horas = m // 60
        m %= 60

        h += horas
        h %= 24

        return h, m, s

    def __add__(self, other):
        h = self.hh + other.hh
        m = self.mm + other.mm
        s = self.ss + other.ss

        t = Time.__ajustar(h, m, s)
        resul = Time(*t)
        return resul
