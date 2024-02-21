class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.h = hh
        self.m = mm
        self.s = ss

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
    pass


if __name__ == "__main__":
    t = Time(1, 5, 7)
    print(t)

    d = Date(1, 4, 2024)
    print(d)
