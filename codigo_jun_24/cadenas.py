"""
Pruebas con cadenas.
- Operadores: + * in
- indices
"""

cad = "hola que tal"
print("La primera letra: ", cad[0])
print("la última:", cad[-1])

cad1 = "hola"
cad2 = "adios"
resul = cad1 + " " + cad2
print(resul)
print(resul * 5)

palabra = input("Dame palabra")
if palabra in resul:
    print(palabra, "está en", resul)
else:
    print("no está")
