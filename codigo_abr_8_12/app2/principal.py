from tiempo import *


if __name__ == "__main__":
    dt = DateTime(10,4,2024, 12,52,9)
    print(dt)
    

    t1 = Time(12, 30, 59)
    t2 = Time(mm=59, ss=10)
    suma = t1 + t2  # suma = t1.__add__(t2)
    print(t1)
    print(t2)
    print(suma)