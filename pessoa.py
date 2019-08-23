class Pessoa:
	def __init__(self,nome,idade,peso,altura):
		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura

		print("Nome:", self.nome)
# almenta a idade da pessoa
	def envelhecer(self):
		print("Idade anterior:", self.idade)
		self.idade = self.idade + 1
		print("Idade atual:", self.idade)
# Almenta o peso da pessoa
	def engordar(self):
		print("Peso anterior:", self.peso)
		self.peso = self.peso + 10
		print("Peso atual:", self.peso)
# Diminue o peso da pessoa
	def emagrecer(self):
		print("Peso anterior:", self.peso)
		self.peso = self.peso - 10
		print("Peso atual:", self.peso)
# Diz se a pessoa ainda cresce ou não 
	def crescer(self):
		if (self.idade < 21):
			print("Altura anterior", self.altura)
			self.altura = self.altura + 0.05
			print("Altura atual:", self.altura)
		else: 
			print("Altura:", self.altura)
			print("Não cresce mais.")
