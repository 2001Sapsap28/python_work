my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('canoli')
friend_foods.append('ice cream')

for food in my_foods:
	print(food.title())


for food in friend_foods:
	print(food.title())
