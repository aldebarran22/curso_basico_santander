import math


def ecuacion(a, b, c):
    raiz = b**2 - 4 * a * c

    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        # return {"x1": x1, "x2": x2}
        return x1, x2
    else:
        raise ValueError(f"Con los parámetros {a},{b},{c} no hay solución")
