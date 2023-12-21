"""
Expresiones regulares en Python
"""
import re, string


def testPatron(patron, L):
    d = {palabra: True if re.match(patron, palabra) else False for palabra in L}
    print("Patrón: ", patron)
    for p, r in d.items():
        print(p, "->", r)
    print()


if __name__ == "__main__":
    testPatron(r".ython", ["python", "Pyton", "Java", "cython", "Jython"])
    testPatron(r"...\.", ["1234.", "abc", "abc.", "hola.", "123."])

    # Validar un DNI:
    testPatron(
        "[0-9]{8}[A-Z]$",
        [
            "12345678a",
            "12345678",
            "123456789S",
            "S",
            "1234A",
            "12345678A",
            "12345678AB",
        ],
    )

    # Validar matrícula europea: 5678FGT
    consonantes = "".join(
        [letra for letra in string.ascii_uppercase if letra not in "AEIOU"]
    )
    patron = r"\d{4}" + f"[{consonantes}]" + "{3}$"
    testPatron(patron, ["1234JYH", "12344AS", "1234bgt", "1234KI"])

    # Validar una hora y coger h, m, y s
    hora = "03:45:36"
    patron = r"([0-2][0-9]):([0-5][0-9]):([0-5][0-9])"
    patron = r"[0-2][0-9]:[0-5][0-9]:[0-5][0-9]"
    obj = re.match(patron, hora)
    if obj:
        print(obj.groups())

    cadena = "La hora de inicio: 03:40:08 y final 04:07:10"
    L = re.findall(patron, cadena)
    print(L)
