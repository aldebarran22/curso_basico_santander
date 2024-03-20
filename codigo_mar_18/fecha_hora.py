class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

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

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


def crearObjeto(clase, *args, **kwargs):
    return clase(*args, **kwargs)

if __name__ == "__main__":
    t1 = Time(1, 23, 5)  # 01:23:05
    print(t1)

    t2 = Time(12, 53, 55)  # 12:53:55
    print(t2)

    suma = t1 + t2  # suma = t1.__add__(t2)
    print(suma)

    d1 = Date(20, 3, 2024)
    print(d1)

    dt = DateTime(20, 3, 2024, 1, 33, 5)  # 20/03/2024 01:33:05
    print(dt)

    print(dt.__class__)
    print(dt.__class__.__name__)

    obj = dt.__class__()
    print(obj)

    t1 = crearObjeto(Time, 12,34,55)
    print(t1, t1.__class__.__name__)

    d1 = crearObjeto(Date, 12,4,2024)
    print(d1, d1.__class__.__name__)
