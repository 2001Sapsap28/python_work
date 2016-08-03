rivers = {
	'nile': 'egypt',
	'hwang ho': 'china',
	'indus': 'india'
}

for river, country in rivers.items():
	print("The " + river.title() + " flows through " +
		country.title())

print("\nRivers: ")
for river in rivers.keys():
	print(river.title())

print("\nCountries: ")
for country in rivers.values():
	print(country.title())