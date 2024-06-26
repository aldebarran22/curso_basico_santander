class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self, other):
        nuevo = Time(self.hh + other.hh, self.mm + other.mm, self.ss + other.ss)
        nuevo.ajustar()
        return nuevo
    
    def ajustar(self):
        pass

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)


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
    t1 = Time(14, 2, 8)
    print(t1)

    t2 = Time(10, 58, 50)
    print(t2)

    suma = t1 + t2  # suma = t1.__add__(t2)
    print('suma: ', suma)