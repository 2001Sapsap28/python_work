def count_words(filename):
	"""Count the approximate number of words in a file"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + 
			" words.")

filename = 'programming.txt'
count_words(filename)

###########Using readlines() method in try-except block###########

#	try: 
#		with open(filename) as f_obj:
#			contents = f_obj.readlines()
#	except FileNotFoundError:
#		msg = "Sorry, the file " + filename + " does not exist."
#		print(msg)
#	else:
#		# Count the approximate number of words in the file.
#		num_words = len(contents )
#		print("The file " + filename + " has about " + str(num_words) + 
#			" words.")
#
#filename = 'programming.txt'
#count_words(filename)

# Output: The file programming.txt has about 4 words.
# Reason: readlines() stores the 4 lines(items) as 4 individual 
# strings, i.e. ["I love programming.", ...]