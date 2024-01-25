class Time:
    def __init__(self, hh=0, mm=0, ss=0):
        # definir los att con acceso privado
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        # Resultado: 15:02:06
        return "%02d:%02d:%02d" % (self.hh, self.mm, self.ss)

    def __repr__(self):
        return str(self)
