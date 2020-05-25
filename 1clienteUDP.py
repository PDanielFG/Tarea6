import socket 
import pickle
import os

HOST = 'localhost'
PORT = 1025

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

txt = "Soy el cliente"
s_udp.sendto(pickle.dumps(txt), (HOST, PORT))

s_udp.close()
