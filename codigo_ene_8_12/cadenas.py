"""
Cadenas en Python:
Secuencias de escape (\n, \t) y cadenas raw.
"""
nombre = "Jorge"
print("hola\nadios")
print("hola\tadios")
print('El nombre es: "', nombre, '"')
print(r"hola\tadios")

# Operadores a nivel de cadena:
print("hola" + nombre)  # Concatenar
print("hola" * 5)  # Concatenar n-veces

# Partir una cadena en campos:
linea = "1;Davolio;Representante de ventas"
cab = "id;nombre;cargo"
L = linea.split(";")
Lcab = cab.split(";")
print(L)
print(Lcab)
# Imprimir el nombre: 
print(L[1])
d = dict(zip(Lcab, L))
print(d)
# Imprimir el nombre: 
print(d['nombre'])