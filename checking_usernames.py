current_users = ['admin', 'Calistoga', 'ClawHammer', 'Capone']

new_users = ['tookewlf0rsK3wl', 'divideByZero', 'Cogenix', 'Capone']

for new_user in new_users:
	if new_user in current_users:
		print("Please enter a new username.")
		print("Username " + new_user.title() + " has been taken.")
	else:
		print("Username available.")