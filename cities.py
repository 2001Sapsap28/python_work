cities = {
	'London': {
		'country': 'England',
		'population': '8.5 million',
		'fact': 'Big Ben is the bell, not the clock tower.'
	},
	'Frankfurt': {
		'country': 'Germany',
		'population': '687,775',
		'fact': 'You can go anywhere across Europe from here.'
	},
}

for city, features in cities.items():
	print(city + ": ")
	print(features['country'])
	print(features['population'])
	print(features['fact'])