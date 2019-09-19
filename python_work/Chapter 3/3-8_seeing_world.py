destinations = ['bali' , 'paris' , 'amsterdam' , 'switzerland' , 'africa']

print(destinations)

print("Here is a sorted version of my destination list:")
print(sorted(destinations))

print("\nHere is the original list again")
print(destinations)

print("\nHere is a reverse sorted list in alphabetical order:")
print(sorted(destinations, reverse = True))

print("\nDon't worry the list is still available in the original order")
print(destinations)

print("\nHere is a version of the list using the reverse() function")
destinations.reverse()
print(destinations)

print("\nHere is the list reversed to its original form:")
destinations.reverse()
print(destinations)

print("\nHere the list sorted using the sort() function:")
destinations.sort()
print(destinations)

print("\nHere's the list sorted in reverse alphabetical order using the sort() function")
destinations.sort(reverse = True)
print(destinations)

