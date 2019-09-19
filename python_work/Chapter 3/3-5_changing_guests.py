dinner_guests = ['Jay Z' , 'Elon Musk' , 'Brian Cranston' , 'Kobe Bryant']
non_guests = dinner_guests.pop(2)

print("Yo " + dinner_guests[0] + " would you like to come to dinner?")
print("Yo " + dinner_guests[1] + " would you like to come to dinner?")

print("Unfortunately " + non_guests.title() + " can't make it tonight, but " + dinner_guests[2].title() + " will be coming instead.")