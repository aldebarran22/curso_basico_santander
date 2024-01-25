"""
Imprimir información en columnas: 
texto, entero y real
"""

import sys


def formatear(L, file=sys.stdout):
    print("%s\t%s\t%s\t%s" % ("producto", "precio", "uds", "total"), file=file)
    for d in L:
        print(
            "%s\t%f\t%d\t%f"
            % (d["producto"], d["precio"], d["uds"], d["uds"] * d["precio"])
        )


if __name__ == "__main__":
    d = [
        {"producto": "portatil", "precio": 566.7, "uds": 2},
        {"producto": "HP", "precio": 1269.34, "uds": 1},
        {"producto": "teclado", "precio": 55.8, "uds": 3},
    ]
    formatear(d)
