"""
Capturar los argumentos de la línea de comandos en Python
Librería: argparse
"""

import sys

# Recuperar los parámetros y comprobar si viene 2 números enteros
L = sys.argv
if len(L) == 3:
    for i in L[1:]:
        if not i.isnumeric():
            print("Se necesitan dos números")
            print("python argumentos.py <<num1>> <<num2>>")
            exit()
else:
    print("Sintaxis incorrecta ...")
    print("python argumentos.py <<num1>> <<num2>>")
