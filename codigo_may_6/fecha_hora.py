class TimeError(Exception):

    def __init__(self, mensaje=""):
        Exception.__init__(self, mensaje)


class Time:

    def __init__(self, hh=0, mm=0, ss=0):

        if not (0 <= hh <= 23):
            raise TimeError(f"No es correcto el valor: {hh} para las horas")

        if not (0 <= mm <= 59):
            raise TimeError(f"No es correcto el valor: {mm} para los minutos")

        if not (0 <= ss <= 59):
            raise TimeError(f"No es correcto el valor: {ss} para las sg")

        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    @staticmethod
    def __ajustar(h, m, s):
        minutos = s // 60
        s %= 60

        m += minutos
        horas = m // 60
        m %= 60

        h += horas
        h %= 24

        return h, m, s

    def __add__(self, other):
        h = self.hh + other.hh
        m = self.mm + other.mm
        s = self.ss + other.ss

        t = Time.__ajustar(h, m, s)
        resul = Time(*t)
        return resul


class Date:

    def __init__(self, dd, mm, yy):
        self.d = dd
        self.m = mm
        self.y = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d, self.m, self.y)

    def esBisiesto(self):
        anyo = self.y
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


class DateTime(Time, Date):
    """Solución por herencia multiple"""

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, hh, mm, ss)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


class DateTime2:
    """Solución por composición"""

    def __init__(self, d=1, m=1, y=1970, hh=0, mm=0, ss=0):
        self.date = Date(d, m, y)
        self.time = Time(hh, mm, ss)

    def __str__(self):
        return str(self.date) + " " + str(self.time)


if __name__ == "__main__":
    try:
        h1 = Time(1, 50, 50)  # 01:05:05
        h2 = Time(23, 45, 50)

        suma = h1 + h2  # suma = h1.__add__(h2)
        print(suma)

        dt = DateTime(8, 5, 2024, 11, 45, 24)
        print(dt)  # 08/05/2024 11:45:24

        dt2 = DateTime2(8, 5, 2024, 11, 45, 24)
        print(dt2)  # 08/05/2024 11:45:24

    except TimeError as e:
        print(e)
