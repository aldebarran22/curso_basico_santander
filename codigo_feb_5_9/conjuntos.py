"""
Operaciones entre conjuntos: Operadores
intersección: &
unión: |
diferencia: -
dif. simétrica: ^
"""

comida = ["Miguel", "Tomás", "Raquel", "Eva", "Raúl"]
cena = ["Tomás", "Eva", "Sandra", "Ana", "Juan"]

c1 = set(comida)
c2 = set(cena)

print("Quien va a comer y a cenar:", c1 & c2)
print("Quienes van solo a comer:", c1 - c2)
print("Quienes van solo a un evento:", c1 ^ c2)
print("Quienes van solo a un evento:", (c1 | c2) - (c1 & c2))
print("Quienes han participado en los eventos:", c1 | c2)
