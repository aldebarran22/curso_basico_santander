# -*- coding: Cp1252 -*-
# ejemplos de objetos:


class TimeError(Exception):
    def __init__(self, mensaje=""):
        Exception.__init__(self, mensaje)


class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        if not (0 <= hh <= 23):
            raise TimeError(f"El valor {hh} no es correcto en las horas")
        if not (0 <= mm <= 59):
            raise TimeError(f"El valor {mm} no es correcto en los minutos")
        if not (0 <= ss <= 59):
            raise TimeError(f"El valor {ss} no es correcto en las segundos")
        
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    @staticmethod
    def horaActual():
        return ""

    @classmethod
    def horaGMT(cls):
        print(cls)
        return ""

    # Getters, Setters.
    def getHH(self):
        return self.__hh

    def setHH(self, hh):
        self.__hh = hh

    def getMM(self):
        return self.__mm

    def setMM(self, mm):
        self.__mm = mm

    def getSS(self):
        return self.__ss

    def setSS(self, ss):
        self.__ss = ss

    def __eq__(self, hora):
        return (
            (self.__hh == hora.__hh)
            and (self.__mm == hora.__mm)
            and (self.__ss == hora.__ss)
        )

    def toSegundos(self):
        return self.__hh * 3600 + self.__mm * 60 + self.__ss

    def ajustar(self):
        minutos = self.__ss // 60
        self.__ss %= 60
        self.__mm += minutos
        horas = self.__mm // 60
        self.__mm %= 60
        self.__hh = (self.__hh + horas) % 24

    def __add__(self, other):
        suma = Time(
            self.__hh + other.__hh, self.__mm + other.__mm, self.__ss + other.__ss
        )
        suma.ajustar()
        return suma

    def __str__(self):
        return "%02d:%02d:%02d" % (self.__hh, self.__mm, self.__ss)

    # Definición de propiedades:
    hh = property(getHH, setHH)
    mm = property(getMM, setMM)
    ss = property(getSS, setSS)


class Date:
    def __init__(self, dd, mm, yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd, self.__mm, self.__yy)

    def esBisiesto(self):
        anyo = self.__yy
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Time, Date):
    def __init__(self, d=1, m=1, y=1970, HH=0, MM=0, SS=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, HH, MM, SS)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    # pruebas con la clase Time
    h1 = Time(8, 78)
    h2 = Time(5, 23, 7)

    h1.horaGMT()
    Time.horaGMT()

    print("h1.hh:", h1.hh)
    h1.hh = 10
    print("h1.hh:", h1.hh)
    exit()
    # 8:39:45 + 5:23:07 = 14:02:52

    print("h1 " + str(h1) + " h2 " + str(h2))
    # print("segundos de h1: " + str(h1.ss))
    suma = h1 + h2  # suma = h1.__add__(h2)
    print("suma: " + str(suma))
    print("suma en sg: " + str(suma.toSegundos()))
    suma.hh = 20
    print("suma: " + str(suma))

    # pruebas con la clase Date:
    d1 = Date(8, 5, 2020)
    if d1.esBisiesto():
        print(d1, " es un año bisiesto")

    # pruebas con la clase DateTime:
    dt = DateTime(31, 5, 2015, 6, 8, 34)
    print(str(dt))  # 31/05/2015 06:08:34
