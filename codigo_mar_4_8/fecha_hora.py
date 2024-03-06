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


class DateTime(Time, Date):

    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, H, M, S)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    t1 = Time(7, 53, 3)
    print(t1)

    t2 = Time(17, 12, 37)
    print(t2)

    suma = t1 + t2  # suma = t1.__add__(t2)
    print("suma: ", suma)

    dt = DateTime(6, 3, 2024, 13, 58, 12)
    print(dt)  # 06/03/2024 13:58:12

    # Crear un objeto a partir de otro:
    t3 = t1.__class__(12)
    print(t3)

    cad = "{}({},{},{})".format("Time", 3, 45, 9)
    print(cad)
    t4 = eval(cad)
    print(t4)

    print(t4.__dict__)
    t4.mlsg = 345
    t4.__dict__["microsg"] = 4578
    print(t4.__dict__)
    print(t4.microsg)
