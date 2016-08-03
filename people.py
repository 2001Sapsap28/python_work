mark_zuckerberg = {
	'first_name': 'mark',
	'last_name': 'zuckerberg',
	'age': '31'
}

elon_musk = {
	'first_name': 'elon',
	'last_name': 'musk',
	'age': '44'
}

batman = {
	'first_name': 'bruce',
	'last_name': 'wayne',
	'age': '--'
}

people = [mark_zuckerberg, elon_musk, batman]

for person in people:
	full_name = person['first_name'] + " " + person['last_name']
	print(full_name.title())
	print("\tAge: " + person['age'])
