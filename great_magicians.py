magician_names = ['alice', 'david', 'criss']

def make_great(magician_names):
	the_great = ' the Great '
	for magician_name in magician_names:
		magician_name += the_great

def show_magicians(magician_names):

	for magician_name in magician_names:
		print(magician_name.title())

make_great(magician_names)
show_magicians(magician_names)