from modulos.fecha import Date
from modulos.hora import Time
from modulos.fechahora import DateTime

if __name__ == "__main__":
    f = Date(1, 2, 2024)
    t = Time(12, 3, 45)
    dt = DateTime()
    print(f, t, dt)
