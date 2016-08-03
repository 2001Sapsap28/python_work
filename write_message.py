filename = 'programming.txt'

# Writing to a file 

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# Appending to a file without overwriting it

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating new apps that can run in a browser.\n")

