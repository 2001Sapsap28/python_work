def city_country():
	city = input("Enter city: ")
	country = input("Enter country: ")
	formatted_output = city + ' ' + country 
	print(formatted_output.title())

# Calling the function at least 3 times
index = 0 
while index in range(3):
	city_country()
	index += 1