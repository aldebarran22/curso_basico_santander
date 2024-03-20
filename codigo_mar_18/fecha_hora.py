class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

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


class DateTime(Date, Time):
    pass


if __name__ == "__main__":
    t1 = Time(1, 3, 5)  # 01:03:05
    print(t1)

    d1 = Date(20, 3, 2024)
    print(d1)

    dt = DateTime(20, 3, 2024, 1, 3, 5)  # 20/03/2024 01:03:05
    print(dt)
