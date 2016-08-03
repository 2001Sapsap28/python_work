class Employee():
	"""Stores information about an employee or give a raise."""

	def __init__(self, first, last, salary):
		self.first_name = first 
		self.last_name = last 
		self.annual_salary = salary

	def give_raise(self, extra=5000):
		if extra:
			self.annual_salary += extra
		else:
			self.annual_salary += extra

		return self.annual_salary 

#employee_0 = Employee('zheng hong', 'tan', 3000)
#print(employee_0.give_raise(400))