class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        # definir los att con acceso privado
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        # Resultado: 15:02:06
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    def __repr__(self):
        return str(self)


class Date:
    def __init__(self, d=1, m=1, y=1970):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d, self.m, self.y)

class DateTime(Time, Date):

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d,m,y)
        Time.__init__(self, hh,mm,ss)

    def __str__(self):
        return Date.__str__(self)+" "+Time.__str__(self)
    
if __name__ == '__main__':
    dt = DateTime()
    print(dt)