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
        self.d = dd
        self.m = mm
        self.y = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d, self.m, self.y)

    def esBisiesto(self):
        anyo = self.y
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Time, Date):
    """Solución por herencia multiple"""

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, hh, mm, ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


class DateTime2:
    """Solución por composición"""

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        self.date = Date(d, m, y)
        self.time = Time(hh, mm, ss)

    def __str__(self):
        return str(self.date) + " " + str(self.time)


if __name__ == "__main__":
    h1 = Time(1, 50, 50)  # 01:05:05
    h2 = Time(23, 45, 50)

    suma = h1 + h2  # suma = h1.__add__(h2)
    print(suma)

    dt = DateTime(8, 5, 2024, 11, 45, 24)
    print(dt)  # 08/05/2024 11:45:24

    dt2 = DateTime2(8, 5, 2024, 11, 45, 24)
    print(dt2)  # 08/05/2024 11:45:24