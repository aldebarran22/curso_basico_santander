from modulos.fecha import Date
from modulos.hora import Time

class DateTime(Time, Date):

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)

class DateTime2:

    def __init__(self,dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        self.date = Date(dd,mm,yy)
        self.time = Time(h,m,s)

    def __str__(self):
        return self.date.__str__() + " " + self.time.__str__()



