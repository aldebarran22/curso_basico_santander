


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

