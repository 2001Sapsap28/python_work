dog = {
	'kind': 'german shepherd',
	'owner': 'john cena'
}

cat = {
	'kind': 'bengal cat',
	'owner': 'mary'
}

reptile = {
	'kind': 'leopard gecko',
	'owner': 'trevor'
}

pets = [dog, cat, reptile]

for pet in pets:
	print(pet['kind'].title())
	print("Owner: " + pet['owner'].title() + "\n")