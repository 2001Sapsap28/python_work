# Store numbers from 1 through 9
numbers = [value for value in range(1, 10)]

for number in numbers:
	if number == 1:
		print("1st ")
	elif number == 2:
		print("2nd ")
	elif number == 3:
		print("3rd ")
	else:
		print(str(number) + "th")