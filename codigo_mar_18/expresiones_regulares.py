"""
Expresiones regulares en Python
"""

import re


def validar(patron, L):
    print("Patrón: ", patron)
    for cad in L:
        print(cad, "True" if re.match(patron, cad) else "False")
    print("-" * 20)


if __name__ == "__main__":
    # Cadenas de 3 caracteres:
    patron = r"...$"
    L = ["***", "1234", "abc", "--a", "12345"]
    validar(patron, L)

    # Cadenas de 3 letras mayúsculas/minúsculas:
    patron = r"[A-Za-z][A-Za-z][A-Za-z]$"
    L = ["***", "1234", "abc", "--a", "AAA", "ABCD", "ASe"]
    validar(patron, L)

    # Cadenas que sólo contengan 3 vocales:
    patron = r"[aeiou]{3}$"
    L = ["aei", "aaae", "abc", "--a", "AAA", "ABC", "Aie"]
    validar(patron, L)

    # Cadenas de 3 números:
    patron = r"[0-9][0-9][0-9]$"
    L = ["***", "1234", "abc", "--a", "AAA", "ABCD", "ASe"]
    validar(patron, L)

    # Cuenta Bancaria: sucursal-entidad-dc-numero
    patron = r"\d{4}-\d{4}-\d{2}-\d{4,10}$"
    L = [
        "1243-4500-99-0123456789",
        "1243-4500-99-0003456789",
        "1243-4500-9-0123456789",
        "1243-4500-990123456789",
    ]
    validar(patron, L)

    # Extraer los campos
    patron = r"(\d{4})-(\d{4})-(\d{2})-(\d{4,10})$"
    obj = re.match(patron, "1243-4500-99-0123456789")
    print(obj.groups())

    patron = r"<h1>(.*?)</h1>"
    html =  "<h1>titulo</h1><h3>subtitulo</h3><h4>subtitulo</h4><h1>hola</h1>"
    for i in re.finditer(patron, html):
        print(i.groups())

    

