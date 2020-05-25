import socket
import os
import pickle

HOST = 'localhost'
PORT = 1025

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_udp.bind ((HOST,PORT))

print ("Me quedo a la espera")
mensaje = s_udp.recv(1024)

print ("Recibido el mensaje ---->"+pickle.loads(mensaje))

s_udp.close()

