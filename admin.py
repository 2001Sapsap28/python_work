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

class Privileges():
	def __init__(self, privileges=["can add post", "can delete post",
		"can ban user"]):
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)


class Admin(User):
	def __init__(self, first_name, last_name, age):
		super().__init__(first_name, last_name, age)
		self.privileges = Privileges()


admin = Admin('tan', 'zheng hong', '18')
admin.privileges.show_privileges() 