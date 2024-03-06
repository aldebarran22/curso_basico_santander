"""
POO en Python
"""

from random import randint
from string import ascii_uppercase


def generarDatos():
    candidatos = [
        {
            "nombre": letra * 3,
            "años": randint(5, 10),
            "numempresas": randint(1, 8),
            "superior": True if randint(2, 10) % 2 == 0 else False,
        }
        for letra in ascii_uppercase
    ]
    return candidatos
