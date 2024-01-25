"""
Imprimir información en columnas: 
texto, entero y real
"""

import sys

def formatear(d, file=sys.stdout):
    print("%s\t%s\t%s\t%s" % ('producto','precio','uds','total'),file=file)

if __name__ == "__main__":
    d = [
        {"producto": "portatil", "precio": 566.7, "uds": 2},
        {"producto": "HP", "precio": 1269.34, "uds": 1},
        {"producto": "teclado", "precio": 55.8, "uds": 3},
    ]
    formatear(d)
