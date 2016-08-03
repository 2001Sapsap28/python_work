class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 23

	def describe_restaurant(self):
		print("Restaurant: " + self.name.title())
		print("Cuisine Type: " + self.cuisine_type.title())

	def set_number_served(self, number):
		self.number_served = number 
		return str(number)

	def increment_number_served(self, number):

		if self.number_served >= 0:
			self.number_served += number
		else:
			print("You can't decrement number served.")

		return str(self.number_served)

	def open_restaurant(self):
		print("This restaurant is open!")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)

	def display_flavors(self, flavors):
		self.flavors = flavors
		print("Flavors: " + str(self.flavors))

IceCreamStand = IceCreamStand('Haagen Dazs', 'ice-cream')

IceCreamStand.describe_restaurant()
IceCreamStand.display_flavors(['vanilla', 'strawberry'])