# -*- coding: Cp1252 -*-
# ejemplos de objetos:

import time

class Time:

    def __init__(self,hh=0,mm=0,ss=0):
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    # Getters, Setters.
    def getHH(self):
        return self.__hh

    def setHH(self,hh):
        self.__hh = hh

    def getMM(self):
        return self.__mm

    def setMM(self,mm):
        self.__mm = mm

    def getSS(self):
        return self.__ss

    def setSS(self,ss):
        self.__ss = ss


   

    def __eq__(self, hora):
        print ("salta eq")
        return (self.__hh == hora.__hh) and (self.__mm == hora.__mm) and (self.__ss == hora.__ss)
    
    def __str__(self):        
        return '%02d:%02d:%02d' % (self.__hh,self.__mm,self.__ss)


    


class Date:

    def __init__(self, dd,mm,yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd,self.__mm,self.__yy)

    def esBisiesto(self):
        anyo = self.__yy    
        if  (anyo % 4 == 0 and anyo % 100 != 0) or (anyo%100 == 0 and anyo % 400 == 0):
            return True    
        else:
            return False

    

# pruebas con la clase Time

h1 = Time(8,39)
h2 = Time(5,23,7)



# 8:39:45 + 5:23:07 = 14:02:52

print ('h1 ' + str(h1) + ' h2 ' + str(h2))
print ('segundos de h1: ' + str(h1.ss))
suma = h1 + h2 
print ('suma: ' + str(suma))
print ('suma en sg: ' + str(suma.toSegundos()))
suma.hh = 20
print ('suma: ' + str(suma))

# pruebas con la clase Date:
d1 = Date(8,5,2020)
if d1.esBisiesto():
    print (str(d1.yy) + " es un año bisiesto")
print (d1)

#pruebas con la clase DateTime:
dt = DateTime(31,5,2015,6,8,34)
print (str(dt))


