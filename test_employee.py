import unittest 
from employee import Employee 

class TestEmployee(unittest.TestCase):

	def setUp(self):
		"""Create default employee instance."""
		self.employee = Employee('zheng hong', 'tan', 7000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(12000, self.employee.annual_salary)

	def test_give_custom_raise(self):
		self.employee.give_raise(400)
		self.assertEqual(7400, self.employee.annual_salary)

unittest.main()