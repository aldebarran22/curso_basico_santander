"""
Conjuntos:
- crear conjuntos
- NO hay acceso directo a los elementos
- Recorrer
- in
- Operadores: & (intersec.), | (unión), - (dif)
- ^ (dif. simétrica)
- Añadir elementos al conjunto: add
"""

c = {1, 1, 1, 1, 2, 3, 5, 6}
print(c)
c.add(1)
c.add(10)
print(c)

# print(c[0]) No tenemos acceso por la posición

for i in c:
    print(i, end=" ")
print()

comida = {"Ana", "Raúl", "Roberto", "Sara", "Olga"}
cena = {"Ana", "Roberto", "Tomás", "Julia", "Paula"}

print("Quien va a comer y a cenar: ", comida & cena)
print("Quien va solo a comer: ", comida - cena)
print("Quien va solo a cenar: ", cena - comida)
todos = comida | cena
print("Quienes han participado en los eventos: ", todos)
print("Cuantos han participado en los eventos: ", len(todos))
print("Quien va solo a un evento: ", comida ^ cena)
