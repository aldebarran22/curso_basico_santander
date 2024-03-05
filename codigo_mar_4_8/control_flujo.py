"""
range, bucle while, break y continue, exit()
"""

# range(ini, fin-1, salto=1)
print(list(range(5)))  # del 0 al 4
print(list(range(1, 11)))  # del 1 al 10
print(list(range(10, 0, -1)))  # del 10 al 1
print(list(range(0, 101, 5)))  # del 0 al 100 de 5 en 5
print(tuple(range(0, 101, 5)))  # del 0 al 100 de 5 en 5

# bucle
"""
while True:
    pass
"""

# Validar una cantidad múltiplo de 10, sin límite de repetición
while True:
    numero = int(input("Teclear importe: "))
    if numero % 10 != 0:
        print("Importe no válido")
    else:
        break
print("Importe: ", numero)

# continue: imprimir del 1 al 10, pero no mostrar del 5 al 7
i = 1
while i <= 10:

    if i == 5:        
        i += 1
        continue

    i += 1
    print(i)
   
i = 0
while i <= 10:
    i += 1
    if i == 5:                
        continue
  
    print(i)