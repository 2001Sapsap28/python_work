print(list(value**2 for value in range(1,11)))

# Tuples
dimensions = (200, 50)
box_dimensions = dimensions[:]

print(box_dimensions)

# If statements
banned_users = ['andrew', 'carolina', 'david']
user = 'carolina'
if user in banned_users:
	print(user.title() + ", you cannot post a response.")

# Returning a dictionary 
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person 

print(build_person('jimi', 'hendrix'))

for key in {'one':1, 'two':2}:
	print(key)