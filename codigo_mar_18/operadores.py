"""operadores.py
Operaciones con variables numéricas
Prioridades: potencia, (div div_ent, resto), suma, resta
""" 

# Calcular la media de dos numeros:
n1 = 34
n2 = 123
media = (n1 + n2)  / 2
print('media: ', media)

# Retirar 230 eur:
importe = 230
numBilletes50 = importe // 50
print('num billetes: ' , numBilletes50)
resto = importe % 50
print('resto: ' , resto)