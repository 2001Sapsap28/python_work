favorite_places = {
	'Mary': ['Budapest', 'Frankfurt', 'Los Angeles'],
	'Andy': ['Moscow', 'Toronto', 'Rome'],
	'Trevor': ['London', 'Seattle', 'Paris']
}

for name, places in favorite_places.items():
	print(name + ": ")
	for place in places:
		print(place)