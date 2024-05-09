


if __name__ == "__main__":
    try:
        h1 = Time(1, 70, 50)  # 01:05:05
        h2 = Time(23, 45, 50)

        suma = h1 + h2  # suma = h1.__add__(h2)
        print(suma)

        dt = DateTime(8, 5, 2024, 11, 45, 24)
        print(dt)  # 08/05/2024 11:45:24

        dt2 = DateTime2(8, 5, 2024, 11, 45, 24)
        print(dt2)  # 08/05/2024 11:45:24

    except TimeError as e:
        print(e.__class__.__name__, e)
