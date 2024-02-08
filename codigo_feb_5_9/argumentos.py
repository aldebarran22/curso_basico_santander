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
    n1 = int(L[1])
    n2 = int(L[2])
    print(f"La suma de {n1} y {n2} es {n1+n2}")

else:
    print("Sintaxis incorrecta ...")
    print("python argumentos.py <<num1>> <<num2>>")
