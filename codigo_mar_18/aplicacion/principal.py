"""
Código principal del proyecto
"""

from modulos.fecha import Date
from modulos.fechahora import DateTime
from modulos.hora import Time


def crearObjeto(clase, *args, **kwargs):
    return clase(*args, **kwargs)


if __name__ == "__main__":
    t1 = Time(1, 23, 5)  # 01:23:05
    print(t1)

    t2 = Time(12, 53, 55)  # 12:53:55
    print(t2)

    suma = t1 + t2  # suma = t1.__add__(t2)
    print(suma)

    d1 = Date(20, 3, 2024)
    print(d1)

    dt = DateTime(20, 3, 2024, 1, 33, 5)  # 20/03/2024 01:33:05
    print(dt)

    print(dt.__class__)
    print(dt.__class__.__name__)

    obj = dt.__class__()
    print(obj)

    t1 = crearObjeto(Time, 12, 34, 55)
    print(t1, t1.__class__.__name__)

    d1 = crearObjeto(Date, 12, 4, 2024)
    print(d1, d1.__class__.__name__)
