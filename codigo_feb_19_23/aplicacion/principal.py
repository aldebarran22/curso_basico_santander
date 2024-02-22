if __name__ == "__main__":
    t = Time(1, 5, 7)
    print(t)

    t2 = Time(10, 55, 56)
    print(t2)

    s = t + t2  # s = t.__add__(t2)
    print(s)

    d = Date(1, 4, 2024)
    print(d)

    dt = DateTime()
    print(dt)
