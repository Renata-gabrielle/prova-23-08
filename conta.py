class Conta_corrente:
	def __init__(self,numero,correntista,saldo):
		self.numero = numero
		self.correntista = correntista
		self.saldo = saldo

		print("Nome:", self.correntista)
		print("Número da Conta:", self.numero)
# Altera a conta do usuario
	def alterar_nome(self,novo_nome):
		self.correntista = novo_nome
		print("Novo nome: ", self.correntista)
# Efetua depositos
	def deposito(self,valor_deposito ):
		self.saldo = self.saldo + valor_deposito
		print("Foi efetuado um deposito de:", valor_deposito)
		print("Seu saldo atual é de:", self.saldo)
# efetua saques
	def saque(self,valor_saque):
		if (valor_saque <= self.saldo):
			self.saldo = self.saldo - valor_saque
			print("Foi efetuado um saque de:", valor_saque)
			print("Seu saldo atual é de:", self.saldo)
		else: 
			print("Seu saque não pode ser efetuado. ")
