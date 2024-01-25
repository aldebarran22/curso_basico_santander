class Date:
    def __init__(self, d=1, m=1, y=1970):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return "%02d/%02d/%04d" % (self.d, self.m, self.y)
