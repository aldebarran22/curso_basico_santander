class Time:
    def __init__(self, hh=0, mm=0, ss=0):
      
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def __str__(self):
        return "%02d:%02d:%02d" % (self.__hh, self.__mm, self.__ss)


class Date:
    def __init__(self, dd, mm, yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.__dd, self.__mm, self.__yy)

  
