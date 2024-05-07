"""
Control de flujo en Python:
- bucle while
"""

"""
# Bucle infinito
while True:
    pass
"""

# Leer un valor de teclado y solo se aceptan
# multiplos de 10:
while True:
    numero = int(input("Teclear importe:> "))
    if numero % 10 != 0:
        print('Solo se aceptan multiplos de 10')
    else:
        break
        