from tiempo.fechahora import DateTime
from tiempo.fecha import Date
from tiempo.hora import Time

if __name__ == "__main__":
    dt = DateTime(7, 2, 2024, 13, 5, 34)  # 07/02/2024 13:05:34
    print(dt)
    dt2 = DateTime()
    print(dt2)

    h1 = Time(12, 50, 30)
    h2 = Time(88, 9, 35)
    r = h1 + h2
    print(r)

    print(Date.__subclasses__())
    print("Datetime es subclase de Time: ", issubclass(DateTime, Time))
    print(dt.__dict__)
