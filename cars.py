cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()

# Sorted in alphabetical order 
print(cars)

# Sorted in reverse alphabetical order
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list: ")
print(cars)

# Sort original list and print output
print(sorted(cars))

# Display original list again 
print(cars)


# Chapter 5
cars = ['audi', 'bmw', 'subaru', 'toyota']
print("\n")

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title()) 