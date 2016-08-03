favorite_languages = {
	'jen': 'python',
	'sarah': 'C',
	'edward': 'ruby',
	'phil': 'python'
}

# Loop to display key-value, key and value pairs

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title())

for name in favorite_languages.keys():
	print(name.title())

for language in favorite_languages.values():
	print(language.title())

