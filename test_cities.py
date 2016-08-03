import unittest 

from city_functions import get_city_country
class CityCountryTestCase(unittest.TestCase):

	def test_city_country(self):
		"""Does 'Santiago, Chile ' work?"""
		city_country = get_city_country('santiago', 'chile', 5000000)
		self.assertEqual(city_country, 'Santiago, Chile Population = 5000000')

unittest.main()