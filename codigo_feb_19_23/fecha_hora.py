class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

    def __add__(self, other):
        resul = Time(self.h+other.h, self.m+other.m, self.s+other.s)
        resul.ajustar()
        return resul
    
    def ajustar(self):
        minutos = self.s // 60
        self.s %= 60
        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h += horas

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)


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
    """01/01/1970 00:00:00"""

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    t = Time(1, 5, 7)
    print(t)

    t2 = Time(10, 55, 56)
    print(t2)

    s = t + t2  # s = t.__add__(t2)
    print(s)

    d = Date(1, 4, 2024)
    print(d)

    dt = DateTime()
    print(dt)
