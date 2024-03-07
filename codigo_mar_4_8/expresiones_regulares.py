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

    # Cadenas de 3 caracteres y que terminan en punto:
    patron = r"...\.$"
    L = ["abc.", "***.", "1234.", "abc.", "--a.", "12345.", "123"]
    validar(patron, L)

    # DNI:
    patron = r"[0-9]{8}[A-Z]$"
    L = ["AWWEE", "51000123", "65000123J", "12345678AA", "12345678b"]
    validar(patron, L)

    """Comprobar la validez del siguiente código:
    Palabra COD o S/N, un guión bajo, 3 vocales mayúsculas, 
    guión bajo y 6 números que no pueden empezar por 0.
    COD_AEE_800959  S/N_UOO_958474"""

    patron = r"(COD|S/N)_[AEIOU]{3}_[1-9][0-9]{5}$"

    L = [
        "COD_AEE_800959",
        "COD_AGE_800959",
        "S/N_UOO_958474",
        "S/N_UOO_058474",
        "S/M_UOO_958474",
        "S/N_UOO_9584749",
    ]
    validar(patron, L)

    # Validar matrículas europeas:
    patron = r"\d{4}[BCDFGHJKLMNPQRSTVWXYZ]{3}$"

    L = ["1234RR(","0045FTF", "5644TT", "123GGT","1234DDRR"]
    validar(patron, L)


    patron = r"\d{4}[BCDFGHJKLMNPQRSTVWXYZ]{3}$"
    obj = re.match(patron, "1234TRTD")
    print(obj)

    html = "<p>hola que tal</p><b>hola</b>"
    patron = "<p>(.+)</p>"
    obj = re.match(patron, html)
    print(obj)
    print(obj.groups())

    fecha = "12/03/2024"
    patron = "([0-3][0-9])/([0-1][0-9])/(\d{4})"
    obj = re.match(patron, fecha)
    print(obj)
    print(obj.groups())