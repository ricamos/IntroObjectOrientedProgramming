class Clothing:
	"""
	Esse class faria mais sentido junto a Clothes_class, porém eu separei para dar mais enfase a modularidade.
	"""

	# attibutes
	def __init__(self, color, size, style, price):
		self.color = color
		self.size = size
		self.style = style
		self.price = price

	# Methods	
	def change_price(self, price):
		self.price = price

	def calculate_discount(self, discount):
		return self.price * (1 - discount)

	def calculate_shipping(self, weight, rate):
		return weight * rate