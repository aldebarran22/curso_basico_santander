class DateTime(Time, Date):

    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        Date.__init__(self, d, m, y)
        Time.__init__(self, H, M, S)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)
