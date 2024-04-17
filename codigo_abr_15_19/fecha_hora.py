class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        tsuma = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        tsuma.ajustar()
        return tsuma

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


if __name__ == "__main__":
    t1 = Time(12, 4, 6)  # 12:04:06
    print(t1)

    t2 = Time(5, 59, 59)
    print(t2)

    suma = t1 + t2  #    20:04:05
    print(suma)

    f = Date(17, 4, 2024)
    print(f)

    dt = DateTime(17, 4, 2024, 14, 37, 21)
    print(dt)  # 17/04/2024 14:37:21
