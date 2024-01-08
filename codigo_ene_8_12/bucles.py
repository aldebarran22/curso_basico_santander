"""
Bucles en Python:
for:
    - Ideal para colecciones
    - Sabemos el número de veces que hay que ejecutarlo.
while
    - Cuando no sepamos el número de veces que hay que ejecutarlo.
    - La validación de un dato.
"""

# for: leer 3 numeros de teclado y sumarlos:
# range(3): -> 0, 1 y 2
suma = 0
for i in range(3):
    numero = int(input(f"Dame numero {i+1}:"))
    #print(numero)
    suma = suma + numero
print(suma)
