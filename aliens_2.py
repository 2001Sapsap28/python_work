# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens
for alien_number in range(30):
	alien_number = {'color': 'green', 'points': '5', 'speed': 'slow'}
	aliens.append(alien_number)

# Change the first three aliens to yellow
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = '10'

# Show the fist 5 aliens 
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created 
print("Total number of aliens: " + str(len(aliens)))