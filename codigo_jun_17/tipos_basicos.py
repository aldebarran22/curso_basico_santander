"""
Tipo de las variables y fuertemente tipado.
Pruebas con variables.
"""

numero = 100
print(numero, type(numero))

numero = numero + 0.5
print(numero, type(numero))

numero2  = "200"
print(numero2, type(numero2))

# print(numero+ numero2)

# Operación con tipos básicos:
resul = 34 + 12.77 + 4+7j
print(resul, type(resul))

s1 = "23.5"
s2 = "90.5"

# Convertir de str a float:
n1 = float(s1)
n2 = float(s2)

resul = float(s1) + float(s2)
print(resul, n1+n2)
print(n1,"+",n2,"=",(n1+n2))

# f-string
print(f"{n1} + {n2} = {n1+n2}")


#Covertir de float a str
cad1 = str(n1)
cad2 = str(n2)
print(cad1 + cad2)

# En Python es False: 0, "" cadena, [] lista vacía, None
numero = 0
if numero:
    # preguntamos: numero distinto de cero
    print('numero != 0')    
else:
    print('numero es cero')

cadena = ""
if cadena:
    print('hay letras')
else:
    print("cadena vacía")



