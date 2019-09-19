video_games = ['zelda' , 'mega man' , 'sonic' , 'metroid' , 'pokemon']

print(video_games)

video_games[0] = "smash brothers"
print("This is the list using the modifying function:")
print(video_games)

print("\nThis is a printout accessing a single element in the list: ")
print(video_games[1])

print("\nThis is a version of the list using the append function:")
video_games.append("monster hunter")
print(video_games)

print("\nThis is a version of the list using the insert function:")
video_games.insert(2, 'lego avengers')
print(video_games)

print("\nThis is a version of the list using the del function:")
del video_games[6]
print(video_games)

print("\nThis is a version of the list using the pop function:")
popped_game = video_games.pop(5)
print(video_games)
print("\nThis is the popped game:" + popped_game)

print("\nThis is a version of the list removing an item by value:")
boring_game = "sonic"
video_games.remove(boring_game)
print(video_games)

print("\nThis is version of the list using the sort function:")
video_games.sort()
print(video_games)

print("\nThis is a version of the list sorting the list in reverse:")
video_games.sort(reverse = True)
print(video_games)

#video_games.sort(reverse = False)
#print(video_games)

print("\nThis is a version of the list using the sorted function")
print(sorted(video_games))

video_games.sort(reverse = False)

print("\nThis is a version of the list using the reverse function:")
video_games.reverse()
print(video_games)

print("\nThis is a version of the list using the len function:")
x = len(video_games)
print(x)