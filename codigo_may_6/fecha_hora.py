class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    def __ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60

        self.mm += minutos
        horas = self.mm // 60
        self.mm %= 60

        self.hh += horas
        self.hh %= 24

    def __add__(self, other):
        resul = Time(self.hh + other.hh, self.mm + other.mm, self.ss + other.ss)
        resul.__ajustar()
        return resul


class Date:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)

    def esBisiesto(self):
        anyo = self.yy
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Date, Time):
    pass


if __name__ == "__main__":
    h1 = Time(1, 50, 50)  # 01:05:05
    h2 = Time(23, 45, 50)

    suma = h1 + h2  # suma = h1.__add__(h2)
    print(suma)

    dt = DateTime(8, 5, 2024, 11, 45, 24)
    print(dt)  # 08/05/2024 11:45:24
