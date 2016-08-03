# Accessing the values to keys in favorite_languages
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

print("The following languages have been mentioned: ")

# Loop to store and sort each language in a set 

for language in sorted(set(favorite_languages.values())):
	print(language.title())


# Nesting to store a list in a dictionary
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print(name.title() + "'s favorite languages are: ")
	for language in languages:
		print("\t" + language.title())
