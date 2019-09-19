dinner_guests = ['Jay Z' , 'Elon Musk' , 'Brian Cranston']


print("Yo " + dinner_guests[0] + " would you like to come to dinner?")
print("Yo " + dinner_guests[1] + " would you like to come to dinner?")
print("Yo " + dinner_guests[2] + " would you like to come to dinner?")

non_guests = dinner_guests.pop(2)
dinner_guests.insert(2, 'Kobe Bryant')

#Brian Cranston can't make it to dinner, let's invite Kobe Bryant instead.
print("\nUnfortunately " + non_guests.title() + " can't make it tonight, but " + dinner_guests[2].title() + " will be coming instead.")
print("Yo " + dinner_guests[2] + " would you like to come to dinner?")


print("\nGood news everyone!! I was able to find a bigger table!")

dinner_guests.insert(0,'ASAP Rocky')
dinner_guests.insert(1, 'Zendaya')
dinner_guests.append('Jhene Aiko')


print("\nYo " + dinner_guests[0] + " would you like to come to dinner?")
print("Yo " + dinner_guests[1] + " would you like to come to dinner?")
print("Yo " + dinner_guests[2] + " would you like to come to dinner?")
print("Yo " + dinner_guests[3] + " would you like to come to dinner?")
print("Yo " + dinner_guests[4] + " would you like to come to dinner?")
print("Yo " + dinner_guests[5] + " would you like to come to dinner?")

print("\nUnfortunately I'm only able to invite two people to dinner")

dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()

print("\nYo " + dinner_guests[0] + " would you like to come to dinner?")
print("Yo " + dinner_guests[1] + " would you like to come to dinner?")

#confirms only 2 guests are left
print(dinner_guests)
