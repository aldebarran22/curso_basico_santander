class Time:

    def __init__(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self, other):
        resul = Time(self.hh + other.hh, self.mm + other.mm, self.ss + other.ss)
        resul.ajustar()
        return resul

    def ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60
        self.mm += minutos

        horas = self.mm // 60
        self.mm %= 60
        self.hh += horas

    def __str__(self):
        # 01:05:56
        #  1: 5:56
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    def __repr__(self):
        return str(self)


class Date:

    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d, self.m, self.y)

    def esBisiesto(self):
        anyo = self.y
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Time, Date):

    def __init__(self, d=1,m=1,y=1970,hh=0,mm=0,ss=0):
        Date.__init__(self, d,m,y)
        Time.__init__(self, hh,mm,ss)
       
    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)

if __name__ == "__main__":
    dt = DateTime(10,4,2024, 12,52,9)
    print(dt)
    

    t1 = Time(12, 30, 59)
    t2 = Time(mm=59, ss=10)
    suma = t1 + t2  # suma = t1.__add__(t2)
    print(t1)
    print(t2)
    print(suma)
