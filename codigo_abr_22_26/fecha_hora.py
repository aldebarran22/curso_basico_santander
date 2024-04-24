class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __ajustar(self):
        minutos = self.s // 60
        self.s %= 60

        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h = (self.h + horas) % 24

    def __add__(self, other):
        obj = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        obj.__ajustar()
        return obj

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


if __name__ == "__main__":
    t = Time(2, 4, 34)
    print(t)

    t2 = Time(12, 14, 51)
    print(t2)

    suma = t + t2  # suma = t.__add__(t2)
    print(suma)
