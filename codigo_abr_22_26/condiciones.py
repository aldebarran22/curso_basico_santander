"""
Condiciones en Python: and, or, not
"""

inf = 10
sup = 20
num = 25

# Saber si num está dentro del intervalo:
if num >= inf and num <= sup:
    print("En el intervalo")
else:
    print("Fuera del intervalo")

if inf <= num <= sup:
    print("En el intervalo")
else:
    print("Fuera del intervalo")
