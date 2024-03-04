"""
Operadores a nivel de cadenas (+, *, in)
"""

cad1 = "123"
cad2 = "456"
print(cad1 + cad2)
print(cad1 * 10)

n1 = int(cad1)
n2 = int(cad2)
print(n1 + n2)
print(n1 * 10)

# Operador in
cad = "hola que tal"
if "hola" in cad:
    print("si está")
else:
    print("no está")
