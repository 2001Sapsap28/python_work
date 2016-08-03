favorite_numbers = {
	'Mary': ['1', '69', '24'],
	'Andy': ['2', '69', '97'],
	'Trevor': ['3', '76', '89']
}

print("Favorite numbers are: \n")

for name, numbers in favorite_numbers.items():
	print(name + ": " + str(numbers))
print("\n")
	#for number in numbers:
	#	print("\t" + number)