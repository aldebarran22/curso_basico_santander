"""
Conectar con la BD sqlite3.
Crear conexiones y cursores. Ejecutar una consulta.
"""

import sqlite3 as dbapi
from os.path import isfile

def consulta(tabla):
    """
    Lista el contenido de la tabla que recibe
    """
    pass

def testConexion(path):
    if not isfile(path):
        raise FileNotFoundError(f"No existe el fichero {path}")
    else:
        # Abrir la conexión:
        con = dbapi.connect(path)
        