"""
Condiciones en Python: and, or, not
"""

inf = 10
sup = 20
num = 12

# Saber si num está dentro del intervalo:
if num >= inf and num <= sup:
    print("En el intervalo")
else:
    print("Fuera del intervalo")

if inf <= num <= sup:
    print("En el intervalo")
else:
    print("Fuera del intervalo")

if num < inf or num > sup:
    print("Fuera del intervalo")
else:
    print("En el intervalo")
    
if not (num >= inf and num <= sup):
    print("Fuera del intervalo")
else:
    print("En el intervalo")

n1 = 10
n2 = 20
if n1 < n2:
    print('el menor es: ', n1)
elif n2 < n1:
    print('el menor es: ', n2)
else:
    print('son iguales')