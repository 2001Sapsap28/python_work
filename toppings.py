requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

###################If-statements###################

# if 'mushrooms' in requested_topping:
# 	print("Adding mushrooms.")
# if 'pepperoni' in requested_topping:
# 	print("Adding pepperoni.")
# if 'extra cheese' in requested_topping:
# 	print("Adding extra cheese.")
# 

##############for-loop to print toppings###########

#for requested_topping in requested_toppings:
#	if requested_topping == 'green peppers':
#		print("Sorry, we are out of green peppers right now.")
#	else:
#		print("Adding " + requested_topping + ".")

requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print ("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")