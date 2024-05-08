class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    def __add__(self, other):
        resul = Time(self.hh + other.hh, self.mm + other.mm, self.ss + other.ss)
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


if __name__ == "__main__":
    h1 = Time(1, 5, 5)  # 01:05:05
    h2 = Time(23, 45, 50)

    suma = h1 + h2  # suma = h1.__add__(h2)
    print(suma)
