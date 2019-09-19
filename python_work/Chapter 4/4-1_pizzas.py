pizzas = ['pepperoni', 'meat lovers', 'stuff crust', 'deep dish']
friend_pizzas = pizzas[:]

friend_pizzas.append('mushroom')

for pizza in pizzas:
	print('My favorite pizzas are: ' + pizza.title() + " pizza!!")
	print('My friend's favorite pizza are:' + friend_pizzas.title() + 'pizza!')