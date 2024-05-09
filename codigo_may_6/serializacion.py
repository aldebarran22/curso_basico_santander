"""
Serializar con python:
pickle -> 1 objeto
shelve -> varios objetos (diccionario)
"""

from random import randint
from string import ascii_letters


def generarDict():
    # Generar una estructura aleatoria, lista de diccionarios, cada dicc representa un candidato.
    candidatos = [
        {
            "nombre": letra * 5,
            "exp": randint(2, 8),
            "emp": randint(1, 6),
            "sup": True if randint(1, 10) % 2 == 0 else False,
        }
        for letra in ascii_letters
    ]
    return candidatos
