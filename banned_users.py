banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user in banned_users:
	print(user.title() + ", you cannot post a response.")
else:
	print(user.title() + ", you can post a response if you wish.")