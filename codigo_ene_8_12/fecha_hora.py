class TimeError(Exception):
    """
    Clase que gestiona los errores con el tiempo.
    """

    def __init__(self, mensaje=""):
        Exception.__init__(self, mensaje)


class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        if not (0 <= hh <= 23):
            raise TimeError("Las horas deben estar entre 0 y 23")

        if not (0 <= mm <= 59):
            raise TimeError("Los minutos deben estar entre 0 y 59")

        if not (0 <= ss <= 59):
            raise TimeError("Los segundos deben estar entre 0 y 59")

        # definir los att con acceso privado
        self.__hh = hh
        self.__mm = mm
        self.__ss = ss

    def ajustar(self):
        minutos = self.__ss // 60
        self.__ss %= 60
        self.__mm += minutos

        horas = self.__mm // 60
        self.__hh += horas
        self.__mm %= 60

    def __add__(self, other):
        resul = Time(
            self.__hh + other.__hh, self.__mm + other.__mm, self.__ss + other.__ss
        )
        resul.ajustar()
        return resul

    def __str__(self):
        # Resultado: 15:02:06
        return "%02d:%02d:%02d" % (self.__hh, self.__mm, self.__ss)

    def __repr__(self):
        return str(self)


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

    try:
        t1 = Time(6, 30, 58)
        t2 = Time(10, 29, 2)
        s = t1 + t2  # s = t1.__add__(t2)
        print("suma: ", s)
    except TimeError as e:
        print(e)

    d1 = Date(12, 5, 2028)
    print(d1)
