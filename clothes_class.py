from general_clothes import Clothing

class Shirt(Clothing):
	"""
	As variaveis (attributes) são importadas de Clothing assim como os metodos. Porém eu posso ter variaveis e metodos individuais para cada class. 
	"""

	def __init__(self, color, size, style, price, country_of_origin):

		Clothing.__init__(self, color, size, style, price) # Inicializa as variaveis (as mesmas de Clothing)
		self.country_of_origin = country_of_origin # Variavel somente de Shirt. Eu poderia ter colocado junto a general_clothes mas para exemplo mantive aqui 

	def double_price(self):
		self.price = 2*self.price


class Pants(Clothing):
	def __init__(self, color, size, style, price, country_of_origin):

		Clothing.__init__(self, color, size, style, price)
		self.country_of_origin = country_of_origin

	def calculate_discount(self, discount):
		return self.price * (1 - discount / 2) 