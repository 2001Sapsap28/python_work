class User():
	def __init__(self, first_name, last_name, age):
		self.first = first_name
		self.last = last_name
		self.age = age 
		self.name = first_name + " " + last_name
		self.login_attempts = 0

	def describe_user(self):
		print("First name: " + self.first.title())
		print("Last name: " + self.last.title())
		print("Age: " + str(self.age))

	def increment_login_attempts(self):
		self.login_attempts += 1
		return str(self.login_attempts)

	def reset_login_attempts(self):
		self.login_attempts = 0
		return str(self.login_attempts)

	def greet_user(self):
		print("Hello, " + self.name.title() + "!")

user_0 = User('zheng hong', 'tan', 18)
user_0.describe_user()
user_0.greet_user()

# Increment login attempts for 3 times 
range = 0
while range <= 2:
	user_0.increment_login_attempts() 
	range += 1 

# Print total login attempts 
print("You have logged in for " + user_0.increment_login_attempts() 
	+ " time(s).")

# Reset and print counter for login attempts 
print(user_0.reset_login_attempts())