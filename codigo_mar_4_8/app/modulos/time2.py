class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

    def __add__(self, other):
        resul = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        resul.ajustar()
        return resul

    def ajustar(self):
        minutos = self.s // 60
        self.s %= 60
        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h = (self.h + horas) % 24

    def __str__(self):
        return "\n".join([k + " " + str(v) for k, v in self.__dict__.items()])

        # return "%02d:%02d:%02d" % (self.h, self.m, self.s)
