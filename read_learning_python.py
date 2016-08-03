filename = 'learning_python.txt'

with open(filename) as file_object:
	# Reading the entire file 
	#contents = file_object.read()
	#print(contents)

	# Looping the file_object
	#for line in file_object:
	#	print(line.strip())

# Storing the lines in a list
	lines = file_object.readlines()

for line in lines:
	print(line.strip())