import socket
import threading
import sys
import pickle

class Cliente():
	def __init__(self, host="localhost", port=3000):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		mensaje_recibido = threading.Thread(target=self.mensaje_recibido)		

		mensaje_recibido.daemon = True
		mensaje_recibido.start()

	
		while True:
			mensaje = input('->')							
			if mensaje != 'salir':
				self.enviar_mensaje(mensaje)				
			else:
				self.sock.close()
				sys.exit()

	def mensaje_recibido(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar_mensaje(self, mensaje):
		self.sock.send(pickle.dumps(mensaje))


c = Cliente()