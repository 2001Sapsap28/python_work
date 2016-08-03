usernames = ['admin', 'tookewlf0rsK3wl', 'divideByZero', 
'Cogenix', 'Yolo5wagg3r']

if usernames: 
	for username in usernames:
		if username == 'admin':
			print("Hello admin! Would you like to see a status report?")
		else:
			print("Hello " + username + "! Thank you for logging in again.")
else:
	print("We need to find some users!")
