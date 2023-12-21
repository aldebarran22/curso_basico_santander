"""
Cliente de socket en Python
"""
import socket

puerto = 8888

s = socket.socket()
print("Se ha creado el socket en el cliente ...")
s.connect(("localhost", puerto))

while True:
    mensaje = input(">")
    s.send(mensaje.encode("utf-8"))
    recibido = s.recv(1024)
    recibido = recibido.decode("utf-8")
    if mensaje == "quit":
        break
print("Fin de cliente")
s.close()
