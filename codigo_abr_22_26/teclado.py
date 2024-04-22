"""
Lectura de variables por teclado y conversiones de tipos:
int()
float()
str()
"""

n1 = input("Dame un número:")
print(n1, type(n1))

n2 = input("Dame otro número:")
if n1.isnumeric() and n2.isnumeric():
    num1 = int(n1)
    num2 = int(n2)
    print(num1 + num2)
else:
    print("Tienen que ser dos enteros!")
