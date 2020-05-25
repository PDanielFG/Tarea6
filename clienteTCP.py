import socket
import os

HOST = 'localhost'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

msg = "hola, eres un servidor"
s.send(msg.encode("utf-8"))

mensaje = s.recv(1024)

print("Recibido: ["+str(mensaje.decode("utf-8"))+"] del servidor")

s.close()