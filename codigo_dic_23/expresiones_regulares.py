"""
Expresiones regulares en Python
"""
import re


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
    testPatron("[0-9]{8}[A-Z]$", \
               ["12345678a","12345678", "123456789S", "S", "1234A", \
                "12345678A", "12345678AB"])
