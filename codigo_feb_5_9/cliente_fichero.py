"""
Cliente TCP en Python
"""

import socket

s = None
fich = None
try:
    s = socket.socket()
    s.connect(("localhost", 9999))
    print("Conectado al Servidor!")
    fich = open("objetos.txt", "r")
    while True:
        mensaje = fich.readline()
        if mensaje:
            mensaje = mensaje.rstrip()
            s.send(mensaje.encode("utf-8"))
            recibido = s.recv(1024)
            recibido = recibido.decode("utf-8")
            print("Recibido:", recibido)
        else:
            break

    s.send("quit".encode("utf-8"))
except Exception as e:
    print(e)
finally:
    if s:
        s.close()
    if fich:
        fich.close()
