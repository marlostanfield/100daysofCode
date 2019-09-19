pizzas = ['pepperoni', 'meat lovers', 'stuff crust', 'deep dish']
friend_pizzas = pizzas[:]

friend_pizzas.append('mushroom')

for pizza in pizzas:
	print('My favorite pizzas are: ' + pizza.title() + " pizza!!")
	
for pizza2 in friend_pizzas:
	print("\nMy friend's favorite pizza are: " + pizza2.title() + ' pizza!')