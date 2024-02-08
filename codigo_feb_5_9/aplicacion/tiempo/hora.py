class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self, other):
        resul = Time(self.hh + other.hh, self.mm + other.mm, self.ss + other.ss)
        resul.ajustar()
        return resul

    def ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60

        self.mm += minutos
        horas = self.mm // 60
        self.mm %= 60

        self.hh += horas
        # self.hh %= 24

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)
