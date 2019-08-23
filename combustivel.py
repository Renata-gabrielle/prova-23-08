class Combustivel:
	def __init__(self,capacidade,preco):
		self.capacidade = capacidade
		self.preco = preco

		print("capacidade da bomba:", self.capacidade)
		print("Preço L:", self.preco)
# Indica quantidade de litros de acordo com o valor
	def abastecer_por_valor(self, valor_abastecimento):
		litros = valor_abastecimento / self.preco
		print("quantidade de litros:", litros)
# Indica o valor de acoedo com a quantidade de litros
	def abastecer_por_litro(self, quantidade_litros):
		litros = quantidade_litros * self.preco
		print("Valor do abastecimento:", litros)
# Modifica o valor do combustivel
	def alterar_preco(self, novo_preco):
		self.preco = novo_preco
		print("Novo Preço:", self.preco)
# Enche a bomba até a sua capacidade
	def encher_bomba(self, reabastecimento):
		self.capacidade = self.capacidade + reabastecimento
		print("Nova capacidade:", self.capacidade)



