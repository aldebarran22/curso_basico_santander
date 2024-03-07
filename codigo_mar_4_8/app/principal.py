from modulos.time2 import Time

if __name__ == "__main__":
    t1 = Time(7, 53, 3)
    print(t1)

    t2 = Time(17, 12, 37)
    print(t2)

    suma = t1 + t2  # suma = t1.__add__(t2)
    print("suma: ", suma)

    dt = DateTime(6, 3, 2024, 13, 58, 12)
    print(dt)  # 06/03/2024 13:58:12
