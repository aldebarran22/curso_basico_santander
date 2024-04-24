class Time:

    # Att. de clase:
    num_instancias = 0

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

        Time.num_instancias += 1

    def __ajustar(self):
        minutos = self.s // 60
        self.s %= 60

        self.m += minutos
        horas = self.m // 60
        self.m %= 60
        self.h = (self.h + horas) % 24

    @staticmethod
    def getNumInstancias():
        return Time.num_instancias

    @classmethod
    def getNumInstancias2(cls):
        return Time.num_instancias

    def __add__(self, other):
        obj = Time(self.h + other.h, self.m + other.m, self.s + other.s)
        obj.__ajustar()
        return obj

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

    def __del__(self):
        Time.num_instancias -= 1


class Date:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)

    def esBisiesto(self):
        anyo = self.yy
        if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 100 == 0 and anyo % 400 == 0):
            return True
        else:
            return False


def make_object(clase, *args, **kwargs):
    return clase(*args, **kwargs)


class DateTime(Time, Date):
    """Uso de la herencia múltiple para crear la clase DateTime"""

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


class DateTime2:
    """Implementación de la clase DateTime por composición"""

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        self.fecha = Date(dd, mm, yy)
        self.hora = Time(h, m, s)

    def esBisiesto(self):
        return self.fecha.esBisiesto()

    def __str__(self):
        return str(self.fecha) + " " + str(self.hora)


def testFechaHora(clase, *args, **kwargs):
    print("Clase: ", clase.__name__)
    dt = clase(*args, **kwargs)
    print(dt)
    if dt.esBisiesto():
        print("El año es bisiesto")
    else:
        print("No es bisiesto")


if __name__ == "__main__":

    testFechaHora(DateTime, 24, 4, 2024, 11, 33, 15)
    testFechaHora(DateTime2, 24, 4, 2024, 11, 33, 15)
    exit()

    print("Num instancias: ", Time.getNumInstancias())
    t = Time(2, 4, 34)
    print(t)

    t2 = Time(12, 14, 51)
    print(t2)

    suma = t + t2  # suma = t.__add__(t2)
    print("Num instancias: ", Time.getNumInstancias())
    print(suma)

    del suma  # Fuerza a llamar al destructor: __del__
    print("Num instancias: ", Time.getNumInstancias())

    print(t.__class__)
    print(t.__class__.__name__)

    obj = t.__class__()
    print(obj)

    obj1 = make_object(Time, 12, 34, 8)
    obj2 = make_object(Date, 12, 3, 2024)
    print(obj1)
    print(obj2)
