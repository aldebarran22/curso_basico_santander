from tiempo.fecha import Date
from tiempo.hora import Time

class DateTime(Time, Date):

    def __init__(self, d=1,m=1,y=1970,hh=0,mm=0,ss=0):
        Date.__init__(self, d,m,y)
        Time.__init__(self, hh,mm,ss)
       
    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)