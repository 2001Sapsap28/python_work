favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

# List of people who should take the languages poll
list_of_people = ['jen', 'phil', 'trevor']

for people in list_of_people:
	if people in favorite_languages.keys():
		print(people.title() + ", thank you for responding.")
	else:
		print(people.title() + ", you are invited to take the poll.")