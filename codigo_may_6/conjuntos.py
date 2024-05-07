"""
Operaciones a nivel de conjunto.
& intersección
| unión (quita repetidos)
- diferencia. Ejemplo: {1,2,3,4} - {3,4,5,6} => {1,2}
^ diferencia simétrica
"""

comida = {"Ana","Gema", "Luis", "Pedro", "Raquel"}
cena = {"Gema", "Luis", "Sofia","Andres", "Sonia"}

print("Quien va a comer y cenar: ", comida & cena)
print("Quien va solo a comer: ", comida - cena)
print("Quien va solo a cenar: ", cena - comida)
print("Quienes han participado en los eventos: ", comida | cena)
print("Va a comer o a cenar pero no a los dos: ", comida ^ cena)

