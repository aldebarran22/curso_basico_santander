"""
Condiciones: operadores relacionales y lógicos.
"""

semaforo = "verde"
if semaforo == "rojo":
    print("parar")

elif semaforo == "verde":
    print("pasar")

else:
    print("precaución")

# Comprobar si un número se encuentra dentro de un intervalo:
ini = 10
fin = 50
numero = 9
if numero >= ini and numero <= fin:
    print(f"El {numero} está dentro del intervalo: {ini},{fin}")
else:
    print("no está en el intervalo")
