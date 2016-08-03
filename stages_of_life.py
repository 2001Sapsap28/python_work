age = 20

if (age < 2):
	status = ' a baby.'
elif (age < 4):
	status = ' a toddler.'
elif (age < 13):
	status = ' a kid.'
elif (age < 20):
	status = ' a teenager.'
elif (age < 65):
	status = ' an adult.'
elif (age > 65):
	status = ' an elder.'

print("You are" + status)