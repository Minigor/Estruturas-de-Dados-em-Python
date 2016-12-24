class Pilha:
	def __init__(self):
		self.armazena = []
	def imprimir(self):
		print(self.armazena)
	def inserir(self, valor):
		self.armazena.insert(0, valor)
	def remove(self):
		if not self.esta_vazia():
			self.armazena.pop(0)
	def tamanho(self):
		return len(self.armazena)
	def esta_vazia(self):
		return self.tamanho() == 0
	


d = Pilha()

d.imprimir()

d.inserir(4)
d.inserir(5)
d.inserir(9)
d.inserir(10)

d.imprimir()

d.remove()

d.imprimir()