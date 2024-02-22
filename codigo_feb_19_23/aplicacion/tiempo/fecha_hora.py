try:
    from tiempo.fecha import Date
    from tiempo.hora import Time
except:
    from fecha import Date
    from hora import Time


class DateTime(Date, Time):
    """01/01/1970 00:00:00"""

    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0, s=0):
        Date.__init__(self, dd, mm, yy)
        Time.__init__(self, h, m, s)

    def __str__(self):
        return Date.__str__(self) + " " + Time.__str__(self)


if __name__ == "__main__":
    dt = DateTime()
    print(dt)
