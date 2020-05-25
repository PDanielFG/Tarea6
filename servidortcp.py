import socket
import threading
import sys
import pickle

class Servidor():
	def __init__(self, host="localhost", port=3000):

		self.clientes = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(5)		

		aceptar = threading.Thread(target=self.accept)
		procesar = threading.Thread(target=self.process)
		
		aceptar.daemon = True
		aceptar.start()

		procesar.daemon = True
		procesar.start()

		while True:
			mensaje = input('->')			
			if mensaje == 'salir':
				self.sock.close()
				sys.exit()
			else:
				pass


	def mensaje_broadcast(self, mensaje, cliente):		
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(mensaje)
			except:
				self.clientes.remove(c)

	def accept(self):		
		print("accept iniciado")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def process(self):				
		print("process iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data, addr = c.recvfrom(1024)
						if data:
							self.mensaje_broadcast(data,c)
					except:
						pass


s = Servidor()