

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __add__(self, other):
        resul = Time(self.hh+other.hh,self.mm+other.mm,self.ss+other.ss)
        resul.ajustar()
        return resul
    
    def ajustar(self):
        minutos = self.ss // 60
        self.ss %= 60
        self.mm += minutos

        horas = self.mm // 60
        self.mm %= 60

        self.hh += horas
        self.hh %= 24

    def __str__(self):        
        return '%02d:%02d:%02d' % (self.hh,self.mm,self.ss)
   

class Date:

    def __init__(self, dd,mm,yy):
        self.d = dd
        self.m = mm
        self.y = yy

   
    def __str__(self):
        return "%02d/%02d/%04d" % (self.d,self.m,self.y)

    def esBisiesto(self):
        anyo = self.y    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False
        
class DateTime(Date, Time):
    pass
        
if __name__ == '__main__':
    hora1 = Time(12,15,5) # 12:06:05
    hora2 = Time(8,45,6) # 08:45:06
    suma = hora1 + hora2 # suma = hora1.__add__(hora2)

    print(hora1)
    print(hora2)
    print(suma)

    d = Date(19,6,2024)
    print(d)

    dt = DateTime(19,6,2024,12,34,12) 
    print(dt) # 19/06/2024 12:34:12



 

