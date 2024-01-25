"""
Imprimir información en columnas: 
texto, entero y real
Redirigir la salida a un fichero o la consola
a partit de un parámetro de la línea de comandos.
"""

import sys


def formatear(L, file=sys.stdout):
    print("%-10s\t%8s\t%3s\t%8s" % ("producto", "precio", "uds", "total"), file=file)
    for d in L:
        print(
            "%-10s\t%8.2f\t%3d\t%8.2f"
            % (d["producto"], d["precio"], d["uds"], d["uds"] * d["precio"]),
            file=file,
        )


if __name__ == "__main__":
    d = [
        {"producto": "portatil", "precio": 566.7, "uds": 2},
        {"producto": "HP", "precio": 1269.34, "uds": 1},
        {"producto": "teclado", "precio": 55.8, "uds": 3},
    ]

    if len(sys.argv) == 1:
        # No hay fichero, lo mandamos a la consola
        formatear(d)
    else:
        fich = open(sys.argv[1], "w")
        formatear(d, fich)
        fich.close()
