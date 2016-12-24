'''
Só muda uma operação em relação a pilha
'''

class Fila:
	def __init__(self):
		self.armazena = []
	def imprimir(self):
		print(self.armazena)
	def inserir(self, valor):
		self.armazena.append(valor)
	def remove(self):
		if not self.esta_vazia():
			self.armazena.pop(0)
		else:
			print("A fila está vazia")
	def tamanho(self):
		return len(self.armazena)
	def esta_vazia(self):
		return self.tamanho() == 0

c = Fila()

c.inserir(1)
c.inserir(4)
c.inserir(12)
c.inserir(54)

c.imprimir()

c.remove()
c.remove()

c.imprimir()