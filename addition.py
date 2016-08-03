def add(num1, num2):
	try:
		number = num1 + num2
	except TypeError:
		print("You cannot add a string.")
	else:
		print(str(number))

add(3, 4)
add(3, 'hi')