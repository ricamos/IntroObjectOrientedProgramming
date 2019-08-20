# from sales_class import Shirt, Pants, SalesPerson
from salesPerson_class import SalesPerson, Shirt, Pants # Mudulo permite importação de Shirt e Pants de SalesPerson porem o codigo está em clothes.
import unittest

class TestClothingClass(unittest.TestCase):
    def setUp(self):
        #self.clothing = Clothing('orange', 'M', 'stripes', 35)
        self.blouse = Shirt('blue', 'M', 'luxury', 40, 'Brazil')
        self.pants = Pants('black', 32, 'baggy', 60, 30)
        
    def test_initialization(self): 
        #self.assertEqual(self.clothing.color, 'orange', 'color should be orange')
        #self.assertEqual(self.clothing.price, 35, 'incorrect price')
        
        self.assertEqual(self.blouse.color, 'blue', 'color should be blue')
        self.assertEqual(self.blouse.size, 'M', 'incorrect size')
        self.assertEqual(self.blouse.style, 'luxury', 'incorrect style')
        self.assertEqual(self.blouse.price, 40, 'incorrect price')
        self.assertEqual(self.blouse.country_of_origin, 'Brazil', 'incorrect country of origin')

    def test_calculateshipping(self):
        self.assertEqual(self.pants.calculate_shipping(.5, 3), .5 * 3,\
         'Clothing shipping calculation not as expected') 
        #self.assertEqual(self.clothing.calculate_shipping(.5, 3), .5 * 3,\
         #'Clothing shipping calculation not as expected') 

        self.assertEqual(self.blouse.calculate_shipping(.5, 3), .5 * 3,\
         'Clothing shipping calculation not as expected') 
    
tests = TestClothingClass()

tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

unittest.TextTestRunner().run(tests_loaded)


def check_results():
    pants_one = Pants('red', 35, 36, 15.12, "Brazil")
    pants_two = Pants('blue', 40, 38, 24.12, "Brazil")
    pants_three = Pants('tan', 28, 30, 8.12, "Brazil")
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
   
    
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()


# Crie objetos e use seus methods
blueShirt = Shirt("Blue", "M", "luxury", "40", "Brazil")
print(blueShirt.calculate_shipping(.5, 3))


# Crie objetos shirt
shirt_one = Shirt("red", "S", "long-sleeve", 25, "Argentina")
shirt_two = Shirt("orange", "L", "short-sleev", 10, "Chile")

# Calcule o valor de uma compra de shirt_one and shirt_two
total = shirt_one.price + shirt_two.price
print(total)

# Calcule descontos
total_discount = shirt_one.calculate_discount(.14) + shirt_two.calculate_discount(.06)
print(total_discount)

# Altere o valor do produto
print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)

# Crie objetos Pants
pants_one = Pants('red', 35, 36, 15.12, "Brazil")
pants_two = Pants('blue', 40, 38, 24.12, "Brazil")
pants_three = Pants('tan', 28, 30, 8.12, "Brazil")

# Crie um objeto vendedor
salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

# faça vendas com o vendedor / substituido sell_pants por sell_clothes
salesperson.sell_clothes(pants_one)    
salesperson.sell_clothes(pants_two)
salesperson.sell_clothes(pants_three)
salesperson.sell_clothes(shirt_one)

# Exiba as vendas 
print(salesperson.display_sales())

# Calcule o total das vendas
print(salesperson.calculate_sales())

# Calcule a comissão
print(salesperson.calculate_commission())

#from clothes_class import * 
