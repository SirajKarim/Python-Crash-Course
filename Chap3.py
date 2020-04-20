# Lists
# 3-1. Names: Store the names of a few of your friends in a list called names . Print
# each person’s name by accessing each element in the list, one at a time.

names = ['Awais','Abdullah', 'Saqib']
print(names[0])
print(names[1])
print(names[2])
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name.
print("Good Evening {0}".format(names[0]))
print("Good night {0}".format(names[1]))
print("Good night {0}".format(names[2]))
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
fav = ["I would like to own toyota car","I would like to own honda bike"]
print(fav[0])
print(fav[1])

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
ges = ['Ajmal','Hamza','Abdal']
inv = ['You are invited for dinner','Come and enjoy dinner with me']
print(ges[0]+" "+inv[0])
print(ges[1]+" "+inv[0])
print(ges[2]+" "+inv[1])
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
ges[2] = 'Ayaz'
print(ges[2]+" "+inv[1])
# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
ges.append('Ausaf')
ges.append('hamid')
ges.append('sohail')
# 46     Chapter 3
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
ges.insert(0,'Abdullah')
ges.insert(2,'Ajju')
ges.append("Akif")
# 3-7. Shrinking Guest List
gests = ['Ahsan','Abdullah','Hasnain']
gests.pop()
gests.remove("Ahsan")
del gests[0]
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
places = ["Saudia","UK","Switzerland","Thailand","Turkey"]
print(places)
# •	 Use sorted() to print your list in alphabetical order without modifying the
# actual list.
print(sorted(places))
# •	 Show that your list is still in its original order by printing it.
print(places)
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
places.reverse()
sorted(places)
print(places)
# •	 Show that your list is still in its original order by printing it again.
places.reverse()
print(places)
# •	 Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
places.reverse()
print(places)
# •	 Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
places.reverse()
print(places)
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
places.sort()
print(places)\
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.
print(len(places))