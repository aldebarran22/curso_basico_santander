
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

