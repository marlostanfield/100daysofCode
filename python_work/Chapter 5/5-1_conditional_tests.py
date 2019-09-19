car = 'subaru'
print("Is car == 'subaru'? I predict True. ")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

cars = ['Audi', 'Bentley', 'Mercedes', 'Pagani']
requested_car = cars[0]

if requested_car != cars[0]:
	print("\nI really want the " +requested_car+ " instead")
else:
	print("\nAwesome, you brought out the " + requested_car)

requested_topping = 'extra cheese'

if requested_topping != 'extra cheese':
	print('\nSend it back and bring it back with extra cheese')
else:
	print('\nExtra chesse just how I like it')

age = 18
if age == 18:
	print("\nWow you're getting old")

age = 19
age_0 = 21

if age <= 19 and age_0 >=20:
	print("\nThe numbers are in alignment")

age_1 = 31
age_2 = 43

if age_1 >=32 or age_2 >= 44:
	print('\nTrue')
else:
	print('\nFalse')

requested_pizzas = ['cheese', 'meat lovers', 'veggie']

if 'cheese' in requested_pizzas:
	print("\nCheese is my favorite pizza")

game_active = True
can_edit = False

print(game_active)
print(can_edit)


