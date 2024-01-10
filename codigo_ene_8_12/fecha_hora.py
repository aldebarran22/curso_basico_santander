class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        # definir los att con acceso privado
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def __str__(self):
        # Resultado: 15:02:06
        return "%02d:%02d:%02d" % (self.__hh, self.__mm, self.__ss)


class Date:
    def __init__(self, dd, mm, yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd, self.__mm, self.__yy)


class DateTime(Time, Date):
    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, hh, mm, ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    dt1 = DateTime(10, 1, 2024, 13, 13, 9)
    print(dt1)
    exit()

    t1 = Time(12, 5, 8)
    print(t1)

    d1 = Date(12, 5, 2028)
    print(d1)
