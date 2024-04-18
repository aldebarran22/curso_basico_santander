
from modulos.hora import Time
from modulos.fecha import Date
from modulos.fechahora import DateTime, DateTime2

if __name__ == "__main__":
    t1 = Time(12, 4, 6)  # 12:04:06
    print(t1)

    t2 = Time(5, 59, 59)
    print(t2)

    suma = t1 + t2  #    20:04:05
    print(suma)

    f = Date(17, 4, 2024)
    print(f)

    dt = DateTime(17, 4, 2024, 14, 37, 21)
    print(dt)  # 17/04/2024 14:37:21

    dt2 = DateTime2(17, 4, 2024, 14, 37, 21)
    print(dt2)  # 17/04/2024 14:37:21
