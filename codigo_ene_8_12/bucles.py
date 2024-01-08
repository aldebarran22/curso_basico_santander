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
"""
suma = 0
for i in range(3):
    numero = int(input(f"Dame numero {i+1}:"))
    # print(numero)
    suma = suma + numero
print(suma)
"""

"""
No es correcto, un int no es iterable!
for i in 3:
    print(i)
"""
# Ejemplo con while, sumar los positivo, con uno negativo terminamos
suma = 0
cuenta = 1
numero2 = int(input("Dame numero:"))
while numero2 > 0:
    suma = suma + numero2  # Acumulador
    cuenta += 1  # cuenta = cuenta + 1 contador
    numero2 = int(input("Dame numero:"))    
print("suma:", suma, 'cuenta: ',cuenta)
