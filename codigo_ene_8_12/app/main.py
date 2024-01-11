from modulos.fecha_hora import DateTime
from modulos.fecha import Date
from modulos.hora import Time, TimeError

if __name__ == "__main__":
    dt1 = DateTime(10, 1, 2024, 13, 13, 9)
    print(dt1)

    try:
        t1 = Time(6, 30, 58)
        t2 = Time(10, 29, 2)
        s = t1 + t2  # s = t1.__add__(t2)
        print("suma: ", s)
    except TimeError as e:
        print(e)

    d1 = Date(12, 5, 2028)
    print(d1)
