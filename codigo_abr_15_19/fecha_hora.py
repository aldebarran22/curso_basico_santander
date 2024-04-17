

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self,other):
          tsuma = Time(self.hh+other.hh, self.mm+other.mm, self.ss+other.ss)
          tsuma.ajustar()
          return tsuma
    
    def ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60
        self.mm += minutos



    def __str__(self):        
        return '%02d:%02d:%02d' % (self.hh,self.mm,self.ss)
class Date:

    def __init__(self, dd,mm,yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd,self.mm,self.yy)

    def esBisiesto(self):
        anyo = self.yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

 
if __name__ == '__main__':
    t1 = Time(12,4,6) # 12:04:06
    print(t1)

    t2 = Time(5, 59, 59)
    print(t2)

    suma = t1 + t2  #    20:04:05
    print(suma)