def get_city_country(city, country, population):

	if population:
		city_country = city + ', ' + country + " population = " + str(population)
	else:
		city_country = city + ', ' + country
	
	return city_country.title()

get_city_country('santiago', 'chile', 5000000)