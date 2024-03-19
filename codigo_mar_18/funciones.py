"""
Funciones en Python
"""

import os


L = os.listdir()
for f in L:
    ext = f.partition(".")[2]
    if ext in ("txt", "py"):
        print(f)
