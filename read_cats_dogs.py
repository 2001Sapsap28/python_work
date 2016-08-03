def read_contents(filename):
	"""Read contents in files"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
#	except FileNotFoundError:
#		print("File " + filename + " not found in this directory.")
	except FileNotFoundError:
		pass
	else:
		print(contents.title())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	read_contents(filename)